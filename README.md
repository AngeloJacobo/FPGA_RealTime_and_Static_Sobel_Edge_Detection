Created by: Angelo Jacobo   
Date: August 22,2021   

# About:  
This project implements a pipelined Sobel Edge Detection design for processing both video and image data using FPGA.
* Video inputs(640x480@30FPS) are retrieved from OV7670 camera and is processed real-time via pipelined convolution module. Threshold value for edge detection is configurable via key[1:0]. key[2] is for alternating display between raw video and edge detected video. **Full codes are on folder "src1"**. 
* Image inputs(640x480) are extracted from jpeg files using Matlab and is sent to FPGA serially. Python script is used to handle the UART protocol. Sobel edge detection is also done by the pipelined convolution module. Below are the sample images and its results. **Full codes and scripts for Matlab and python are on folder "src2"** 


# Inside the src1 folder are:   
* top_module.v -> Combines the camera_interface, sdram_interface, and vga_interface modules.    
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; key[1:0] for increasing/decreasing threshold value for Sobel edge detection  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; key[2] to change display between raw video or edge detected video  
* camera_interface.v -> Configures the register of OV7670 via SCCB protocol. Pixel data is retrieved from      
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;the camera and then passed to asyn_fifo    
* sdram_interface.v -> Controls logic sequence for storing the pixel data retrieved from the camera_interface  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;and sobel_convolution, then sending it to the asyn_fifo connected   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;to vga_interface   
* vga_interface.v -> Passes the pixel data retrieved from sdram to the vga_core 
* sobel_convolution.v -> Pipelined convolution logic. Pixel data from camera asyn_fifo are retrieved, processed,  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;and then sent to asyn_fifo of vga_interface  
* asyn_fifo.v -> FIFO with separate clock domains for read and write. Solves the clock domain crossing issue(see    
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; image below)        
* i2c_top.v -> Bit-bang implementation of SCCB(which is very similar to i2c)     
* sdram_controller.v -> Controller for storing to and retrieving data from SDRAM. Optimized to a memory     
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; bandwidth of 316MB/s     
* vga_core.v -> VGA controller. Set at 640x480 @ 60fps     
* top_module.ucf -> Constraint file for top_module.v      

# Inside the src2 folder are:   
* top_module.v -> Combines the sdram_interface, vga_interface, and UART modules.    
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; key[1:0] for increasing/decreasing threshold value for Sobel edge detection    
* sdram_interface.v -> Stores the pixel data processed by sobel_convolution module and   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;then sending it to the asyn_fifo connected to vga_interface  
* vga_interface.v -> Passes the pixel data retrieved from sdram to the vga_core 
* uart.v -> UART driver. Set to a baud rate of 100_000 (115_200 produce data errors)      
* sobel_convolution.v -> Pipelined convolution logic. Pixel data from uart are retrieved, processed, and then sent to   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;asyn_fifo of vga_interface    
* asyn_fifo.v -> FIFO with separate clock domains for read and write. Solves the clock domain crossing issue(see     
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; image below)         
* sdram_controller.v -> Controller for storing to and retrieving data from SDRAM. Optimized to a memory     
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; bandwidth of 316MB/s     
* vga_core.v -> VGA controller. Set at 640x480 @ 60fps     
* top_module.ucf -> Constraint file for top_module.v    


# Logic Flow:
![Camera_Interface](https://user-images.githubusercontent.com/87559347/130389015-2589d32d-d43d-437a-9a33-820c14e3ee12.jpg)

# Image Edge Detection Results:

<img src="https://user-images.githubusercontent.com/87559347/130393017-6cbd5ce5-a6d0-4ab6-aeff-dceb56d9c016.jpg" width="425"> <img src="https://user-images.githubusercontent.com/87559347/130393321-8e9bd069-08fe-4043-bcc4-4fac97f26839.jpg" width="500"> 

#

<img src="https://user-images.githubusercontent.com/87559347/130393679-1a077ae4-ecc8-4a8c-8bf7-e6d688d83f6d.jpg" width="425"/> <img src="https://user-images.githubusercontent.com/87559347/130393685-84e9d216-fdde-43b3-a20c-6d10c44b605f.jpg" width="500"> 

#

<img src="https://user-images.githubusercontent.com/87559347/130394326-04afa419-479c-4db3-ab97-c7c41a29e359.jpg" width="425"/> <img src="https://user-images.githubusercontent.com/87559347/130394347-4081ecf3-e7ec-474e-bcb0-d92d8d34b76d.jpg" width="500"> 




# Donate   
Support these open-source projects by donating  

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate?hosted_button_id=GBJQGJNCJZVRU)


# Inquiries  
Connect with me at my linkedin: https://www.linkedin.com/in/angelo-jacobo/
