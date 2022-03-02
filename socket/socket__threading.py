'''
threading application with thread-safe approach
a server creates unique socket for every client but receiving and sending data using same socket in that connection
thread-safe approach make guaranty for safe comunication and data loss
'''
## TCP server class
from threading import Thread, Lock
import socket


class Server(Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self.lock = Lock() #for thread-safe
        self.HOST = host
        self.PORT = port
        self.thread_list = [] #collecting threads
        
    def msg_handle(self, msg):
        '''
        do some detailed msg work
        '''
        pass
       
    def client_handle(self, conn, addr):
        '''
        every client run own app, in here standard socket application
        '''
        while True:
            msg = conn.recv(1024).decode('utf-8') #blocking function until message comes
            if msg:
                conn.send(msg.encode('utf-8')) #as example server echo msg sending
        
    
    def socket_send(self, msg:str, sock:socket.socket):
        '''
        created for thread-safe data sending, for future usage
        '''
        with self.lock:
            sock.send(msg.encode('utf-8'))
    
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            try:
                self.sock.bind((self.HOST,self.PORT)) # bind the socket to address
                self.sock.listen(5)
                while True:
                    conn, addr = self.sock.accept() #blocking function until connection established 
                    thread_client = Thread(target=self.client_handle, args=(conn, addr))
                    thread_client.start() #client created
                    self.thread_list.append(thread_client) 
                
            except (KeyboardInterrupt, SystemExit):
                print ('\n! Received keyboard interrupt, quitting threads. << SOCKET - WHILE LOOP >> \n')
                self.cancel()
            except Exception as e:
                print (f'unexpected socket error: {e}')  
                self.cancel()        
                
                
    def cancel(self):
        for thread in self.thread_list:
            thread.cancel()


## TCP client class
# from threading import Thread, Lock
# import socket


class Client(Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self.lock = Lock() #for thread-safe
        self.HOST = host
        self.PORT = port
        self.thread_list = [] #collecting threads
        
        
    def msg_handle(self, msg):
        '''
        do some detailed msg work
        '''
        pass
    
    def socket_send(self, msg:str, sock:socket.socket):
        '''
        created for thread-safe data sending, for future usage
        '''
        with self.lock:
            sock.send(msg.encode('utf-8'))
    
    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
                while True:
                    with self.lock: #other lock/release alternative for syn threading
                        msg = self.sock.recv(1024).decode('utf-8') 

                    if msg:
                        #then create analyses thread here .... dont waste time for scrapping and wait next package ...
                        thread_msg = Thread(target=self.msg_handle, args=(msg,))
                        thread_msg.start()

                
        except Exception as e:
            if e == KeyboardInterrupt or SystemExit:
                print ('\n! Received keyboard interrupt, quitting threads. << SOCKET - WHILE LOOP >> \n')
            else:
                print (f'unexpected socket error: {e}')  
            self.cancel()        
                
                
    def cancel(self):
        for thread in self.thread_list:
            thread.cancel()
