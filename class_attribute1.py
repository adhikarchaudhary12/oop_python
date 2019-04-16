#adding methods

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def substract(self):
        result=self.x-self.y
        return result

p = Point(1,2)
q = Point(3,4)

print(p.x,p.y)
print(q.x,q.y)

print("After editing ")
p.x=1
p.y=2
print(p.x,p.y)