## some test scenerios ##

from threading import Timer,Thread,Event


class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

def printer():
    print('ipsem lorem')
    
def other_fun():
    print('other function')

t = perpetualTimer(1,printer)
t2 = perpetualTimer(5, other_fun)
try:
  t.start()
  t2.start()
except (KeyboardInterrupt, SystemExit):
  print ('\n! Received keyboard interrupt, quitting threads.\n')
#   t.cancel()
#   t2.cancel()