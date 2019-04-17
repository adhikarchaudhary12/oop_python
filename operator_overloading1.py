#overloading+operator

class Point:
    def __init__ (self, x=0,y=0):
        self.x=x
        self.y=y
    def __add__ (self,other):
        x= self.x+other.x
        y= self.y+other.y
        return Point(x,y)

p = Point(1,2)
q = Point(3,4)

return_object = p+q
print(return_object.x, return_object.y)
