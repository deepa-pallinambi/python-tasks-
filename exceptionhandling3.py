try:
    a=int(input("enter a list of integers"))
    print(a)
    c=0
    for i in a:
        c+=i
        print(c)
        l=len(a)
        avg=c//l
        if len(w)==0:
            raise ValueError
        else:
            print(avg)
except:
    print("enter some numbers")
finally:
    print("the programme has finished running")
