#printing objects using __str__

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        result = "X value is {} and y is {}"
             .format(self.x,self.y)
        return result
p = Point(1,2)
print(p)