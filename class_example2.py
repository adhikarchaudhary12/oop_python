#passing parameters to constructor

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(1,2)
q = Point(3,4)

print(p.x)
print(p.y)
print(q.x)
print(q.y)