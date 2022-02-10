from threading import Thread, Timer, Event
import socket 


class SocketThread(Thread):
    def __init__(self):
        Thread.__init__(self) #super().__init__(self)

