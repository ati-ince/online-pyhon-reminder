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

def client_handle(conn:socket.socket, addr):
    print(f'!!! client handler , conn: {conn} , addr: {addr}')
    
    # first send some message ..... for welcoming 
    conn.send('Welcome to the Server !'.encode('utf-8'))
    while True:
        msg = conn.recv(1024).decode('utf-8')
        if msg:
            if msg == '!ConnectionClosed!':
                print(f'serv-client port closing: addr: {addr} !!!')
                break
        
    conn.close() #important dont forget to close() serv-client socket 

with socket.socket(family=socket.AF_INET, type=s_type) as server:
    #some basic network informations
    print(f'server started.')
    # -----------------------------------
    server.bind((HOST, PORT))
    server.listen(5)
    try:
        while True:
            print(f'server waiting connection, host: {HOST}, port: {PORT} ...')
            connection, addr = server.accept()
            #when accept a client in the network lets check information forst 
            peer_name = connection.getpeername()
            sock_name = connection.getsockname()
            sock_timeout = connection.gettimeout()

            print(f'new client connected, address: {addr}')
            print(f'peer name: {peer_name}')
            
            # create new thread for 
            thread = threading.Thread(target=client_handle, args=(connection,addr))
            thread.start()
            print(f'new client thread is started... active client thread number: {threading.active_count()-1}')
    except KeyboardInterrupt:
        print ('Keyboard interruption !!!')

