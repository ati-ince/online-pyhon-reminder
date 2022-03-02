## step-by-step summary ...

'''
family here used IPv4 == AF_INET; 
type is for TCP, if you want to use UDP -> SOCK_DGRAM
''' 
## basic echo - server 
import socket

HOST, PORT = '127.0.0.1', 1234
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as sock:
    sock.bind((HOST,PORT)) # connect to address 
    sock.listen()#max 5 in buffer
    while True:
        conn, addr = sock.accept() #blocking function until connection established 
        with conn:
            msg = conn.recv(1024).decode('utf-8') #blocking function until message comes
            if msg:
                conn.send(msg.encode('utf-8'))
            #the automatically conn closed
        
## basic echo- client
import socket 

HOST, PORT = '127.0.0.1', 1234
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as sock:
    #client.settimeout(3) dont forget to set timeout 
    sock.connect((HOST,PORT))
    msg = sock.recv(1024).decode('utf-8')
    if msg:
        sock.send(msg.encode('utf-8'))
    #the automatically sock closed 
    
    
    
    
    
    
