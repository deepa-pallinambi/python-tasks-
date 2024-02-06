class shape():

    def __init__(self,a):
        self.o=a
        print("name of the shape is",self.o)

    def area(self,a):
        print("this is the area of ",self.o)
    def perimeter(self,a):
        print("this is the perimeter",self.o)

class rectangle(shape):
    def __init__(self,l,b,name):
        print(l,"is the length and",b,"is the breadth of the rectangle",name)
        self.x=l
        self.y=b
        self.z=name
    def areaofrectangle(self,name):
            print("the area of the rectangle",self.z, "is",self.x*self.y)
    def perimeterofrectangle(self,name):
            print("the perimeter of the rectangle",self.z,"is",2*(self.x+self.y))

c=shape("Triangle")
print(c.area("Triangle"))
print(c.perimeter("Triangle"))
c1=rectangle(10,2,"abcd")
print(c1.areaofrectangle("abcd"))
print(c1.perimeterofrectangle("abcd"))

