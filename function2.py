def add(a,b=10,c=None):
    if c== None :
        print(a+b)
    else:
        print(a*b*c)
add(2)
add(2,10,3)
add(2,3)
add(2,c=25,b=5)
add(5,c=25)
add(3,7,8)
add(c=12,a=4)