import socket
import threading
import time

server_type = 'TCP'

if server_type == 'TCP':
    s_type = socket.SOCK_STREAM
elif server_type == 'UDP':
    s_type = socket.SOCK_DGRAM
else:
    raise NotImplementedError('Other socket() communication protocols doesn\'t supported !!!')

HOST, PORT = '127.0.0.1', 9999

def message_handler(conn:socket.socket, msg):
    print('!!! message handler run ')
    print(f'msg: {msg}')
    if len(msg)>0:
        conn.send('!ConnectionClosed!'.encode('utf-8'))

        
with socket.socket(family=socket.AF_INET, type=s_type) as client:
    client.connect((HOST,PORT))
    print('client connected to server !!!')
    while True:
        msg = client.recv(1024).decode('utf-8')
        if msg:
            thread = threading.Thread(target=message_handler, args=(client,msg))
            thread.start()
        
    client.close()
    
    
 # create new thread for 
