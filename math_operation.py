def area():
    print("calculating area of different shapes")
    s=input("enter a shape from circle,rectangle,triangle")
def area_circle():
    r=float(input("enter radius of the circle"))
    pi=3.14
    a1=pi*(r**2)
    print("area of the circle is",a1)
def area_rectangle():
    l=float(input("enter the length of the rectangle"))
    b=float(input("enter the breadth of the rectangle"))
    a2=l*b
    print("area of the rectangle is",a2)

def area_triangle():
     b=float(input("enter the base length of the triangle"))
     h=float(input("enter the height of the triangle"))
     a3=b*h
     print("area of the triangle is",a3)
