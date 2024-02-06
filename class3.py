class vehicle :
    def __init__(self,make,model,year):
        self.x=make
        self.y=model
        self.z=year
    def method_description(self,make,model,year):
        print("this is a vehicle of", self.x , self.y , "of the year",self.z)

class car(vehicle):
    def details(self):
        print("enter the details of the car")

class motorbike(vehicle):
    def details2(self):
        print("enter the details of the motorbike")



g=car("maruti","alto","2012")
g.details()
g.method_description("maruti","alto","2012")
h=motorbike("honda","activa","2015")
h.details2()
h.method_description("honda","activa","2015")
