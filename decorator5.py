def star(func):
    def inner(msg):
        print("*"*30)
        func(msg)
        print("*"*30)
    return inner

def percent(func):
    def inner(msg):
        print("%"*30)
        func(msg)
        print("%"*30)
    return inner

    @star
    @percent
    def printer(msg):
        print(msg)
    print("Hello")