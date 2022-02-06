from threading import Thread, Timer, Event

class MyClass(Thread):
    def __init__(self, name: str,t = 1):
        Thread.__init__(self)
        self.name = name
        self.t = t  
        # self.e = Event()
        self.thread = Timer(self.t,self.handle)

    def handle(self):
        self.hello()
        self.thread = Timer(self.t,self.handle)
        self.thread.start()
    
    def hello(self):
        print('hello')

    def run(self) -> None:
        self.thread.start()

    def cancel(self):
        self.thread.cancel()

thread = MyClass('ati', 1)
thread.start()


        