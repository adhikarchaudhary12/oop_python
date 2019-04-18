#decorating function  with parameters

def smart_divide(func):
    def inner(a,b):
        if b == 0:
            print("Cannot divide by zero")
            return None
        return func(a,b)
    return inner


@smart_divide
def divide(a,b):
    return a/b

result = divide(6,2)
print(result)