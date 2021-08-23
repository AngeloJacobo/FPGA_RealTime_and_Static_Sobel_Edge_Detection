# Instructions for Sending Image data to FPGA via UART:
1. Open "read_image.m" in Octave/Matlab. On the first line, change the file name according to the image file you want to transfer to FPGA. The image must be 640x480. Include the directory if the image is not in the default directory of your Matlab/Octave.
2. Run "read_image.m". The script will display the resolution of the image and it must be "480 640". If its not, edit your image to exact 640x480 using paint or photoshop.
3. The script will make a new file on the default directory named "image.txt" that contains all pixel data.
4. Edit "write_image.py" using notepad, change the file directory based on the exact location of "image.txt". Configure the port and baudrate.
5. Run write_image.py in bash
6. The script will return the total number of bytes sent. Since image is 640x480 and is on grayscale, the result returned must be 307200 (640\*480)

# NOTE: The image that will be sent to FPGA will already be in grayscale.





