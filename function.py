def calculator():
    print ("enter two numbers and select an operation from 1,2,3,4")
    print("""
    \n1=addition\n
    \n2=subtraction\n
    \n3=multiplication\n
    \n4= division\n""")
calculator()
n1=float(input("enter a number"))
n2=float(input("enter another number"))
c=int(input("enter an operation from 1,2,3,4"))
if c==1:
    print("addition of" ,n1 ,"and", n2, "is",n1+n2)
elif c==2:
    print("subtractin of", n1 ,"and", n2 ,"is", n1-n2)
elif c==3:
    print("multiplication of" ,n1 ,"and", n2, "is", n1*n2)
elif c==4:
    print("division of", n1 ,"and", n2, "is",n1//n2)
else:
    print("invalid input")



