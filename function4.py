def mul(*a,b=1):
    c=1
    for i in a:
        c*=i
        d=c*b
    print(d)
mul(10,2,3)
mul(10,2,3,b=5)
mul(10,20)


