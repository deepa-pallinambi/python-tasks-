def greetings():
    a=input("enter your name")
    print("selct a language form 1,2,3")
    print(""" \n1 = "English"\n
              \n2= "malayalam"\n
              \n3 = "hindi"   \n""")
    c=int(input("choose a number from 1,2,3"))
    if c==1:
        print("hello",a, "warm welcome")
    elif c==2:
            print(a,"thankalkk hrdyamaya swagatham")
    elif c==3:
            print(a,"aapka hardik swaagath hai")
greetings()



