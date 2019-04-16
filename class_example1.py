class Point:
    """point clas represents and manipulates x,y coords."""
    def __init__(self): #every class can hae a special function \
    
        self.x = 0
        self.y = 0

    #p and q are objects
    #no neews to pass self

    p=Point() #instantiate an object of type point
    q=Point() #make a second point

    #accessing objects property
    #each object has its own x and y

    print(p.x)
    print(p.y)
    print(q.x)
    print(q.y)
    