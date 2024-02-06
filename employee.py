class Employee:
    def __init__(self,name,salary):
        self.x=name
        self.y=salary
    def get_name(self,name):
         print("hi",self.x)
    def get_salary(self,salary):
         print("your salary is",self.y)
c=Employee("arun","10000")
c.get_name("arun")
c.get_salary("salary")

