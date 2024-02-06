#write a decor function that prints the execution time of a function
import time
def decor(func):
    def wrap(*n):
        start=time.time()
        print(start)
        c=list(func(*n))
        print(c)
        end=time.time()
        print(end)
        execution_time=end-start
        for i in c:
            print("execution time is",execution_time)
            return c
    return wrap
@decor
def l(*n):
    return n

c=l("hi","hello")


