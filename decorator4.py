def first_decorator(func):
    def inner():
        print("Decorating by first decorator")
        func()
    return inner

def second_decorator(func):
    def inner():
        print("Decorating by second decorator")
        func()
    return inner

@first_decorator
@second_decorator
def printer():
    print("inside printer function")
printer()