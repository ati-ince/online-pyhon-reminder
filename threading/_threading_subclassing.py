from threading import Thread, Event
import time


class ThreadObj(Thread):
    '''
    start -> clear -> wait can control the thread lifetime and activation
    set: flag:True control event 
    clear: flag:False
    wait: blocking function until flag:True -> useful for event/thread
    is_set: chek flag state
    '''
    def __init__(self, group=None, target=None, name=None, args=..., kwargs=None, *, daemon=False):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.e = Event()
        print('** event obj state:', self.e.is_set())
        self.e.set()

    def run(self):
        num = 0
        while self.e.is_set():
            print(num, 'hello')
            time.sleep(1)
            num += 1
            self.e.wait()

    def stop_print(self):
        self.e.clear()

    def start_print(self):
        self.e.set()


thread_exp = ThreadObj()

thread_exp.start()

time.sleep(5)
print('second')

thread_exp.stop_print()

print('third')
time.sleep(2)
print('4th')
thread_exp.start_print()
print('5th')
time.sleep(2)
print('6th')
thread_exp.stop_print()
print('7th')
time.sleep(5)
thread_exp.start_print()
print('8th')
