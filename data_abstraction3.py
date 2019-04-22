#private member

class Employee:
    def __intit__(self,name):
        self.__salary= 2000
        self.name= name
        

e1= Employee("Ram")
print(e1.__salary)