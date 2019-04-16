#object aliasing

def modify(obj):
    obj.x = 5

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

p=Point(1,2)
modify(p)
print(p.x,p.y)