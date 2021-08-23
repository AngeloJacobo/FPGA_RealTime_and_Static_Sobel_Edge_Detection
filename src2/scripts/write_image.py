import serial
try:
	fhand=open(r"E:\Desktop\image.txt") #location of image
except: 
	print("File not found")
	exit()
byte_array=bytearray()
for line in fhand:
	line=line.split() #split by space
	for hex in line:
		hex=int(hex,16) #interpret hex as int with base16(hexadecimal)
		byte_array.append(hex)

#starts sending hex data serially
try:
	port=serial.Serial(port="COM3",baudrate=100000,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE) #configure as you like
except:
	print("Error on opening port")
	exit()
count=port.write(byte_array)
print('Data Count: ',count) #number of bytes sent
	
	