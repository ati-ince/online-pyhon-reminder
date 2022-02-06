from threading import Thread, Timer, Event

class MyClass(Thread):
    def __init__(self, name: str):
        Thread.__init__(self)
        self.parameters = dict()
        self.name = name
        self.t_alive = 1.0
        self.t_check = 2.0
        self.t_referancing = 3.0 

        self.thread_alive = Timer(self.t_alive,self.handle_alive)
        self.thread_check = Timer(self.t_check,self.handle_check)
        self.thread_referancing = Timer(self.t_referancing,self.handle_referancing)

    def handle_alive(self):
        self.alive_msg()
        self.thread_alive = Timer(self.t_alive,self.handle_alive)
        self.thread_alive.start()
    
    def handle_check(self):
        self.check_param()
        self.thread_check = Timer(self.t_alive,self.handle_check)
        self.thread_check.start()
    
    
    def handle_referancing(self):
        self.referancing_robot()
        self.thread_referancing = Timer(self.t_referancing,self.handle_referancing)
        self.thread_referancing.start()

    def alive_msg(self):
        print('hello I am Alive MTF !!!')
    
    def check_param(self):
        print('checking parameteras !!!')

    def referancing_robot(self):
        print('Robo ref!!!')

    def run(self) -> None:
        self.thread_alive.start()
        self.thread_check.start()
        self.thread_referancing.start()

    def cancel(self):
        self.thread_alive.cancel()
        self.thread_check.cancel()
        self.thread_referancing.cancel()


thread = MyClass('igus')
try:
    thread.start()
except (KeyboardInterrupt, SystemExit):
  print ('\n! Received keyboard interrupt, quitting threads.\n')
  thread.cancel()
