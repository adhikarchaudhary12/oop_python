def make_pretty(func):
    def inner():
        func()
        print("I got decorator")
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()