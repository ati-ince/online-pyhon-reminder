import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp 

HOST = socket.gethostbyname('www.google.com')
PORT = 80

soc.connect((HOST,PORT)) #as client
print('socket comnneted: ', HOST)
