class Singleton(Exception):
    __single = None
    def __init__(self):
        if Singleton.__single:
            raise Singleton.__single
        Singleton.__single = self
        

single1 = Singleton()
print(single1)

single2 = Singleton()
print(single2)