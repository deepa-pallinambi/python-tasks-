#write a decor function that logs the argument and return the value of the function
def decor(func):
    def wrap(*n):
        a,b=func(*n)
        print("calling",(func),"with arguments",{a,b})
        result=a*b
        print("result is",result)
        return result
    return wrap
@decor
def multiply_numbers(x,y):
    return x,y

s=multiply_numbers(10,2)
b=multiply_numbers(2,3)
c=multiply_numbers(5,8)

