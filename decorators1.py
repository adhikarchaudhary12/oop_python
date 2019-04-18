def make_pretty(func):
    def inner():
        func()
        print("I got decorated")
    return inner

def ordinary():
    print("I am decorated")
#calling a function directly
print("Calling function directly")
ordinary()



#using the concept of decorator
pretty = make_pretty(ordinary)
print("Using decorator...")
pretty()