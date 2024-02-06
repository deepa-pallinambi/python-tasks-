
y=input("enter a filename")
try:
    with open("y","w") as f:
        f.writelines("hi")
        print("run successfully")
        with open("hiii.txt","r") as g:
            print(g.read())
except:
    print("error occured")




