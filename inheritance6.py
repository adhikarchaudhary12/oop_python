class Animal:
    def speak(self):
        print("Animal speaking")

class Dog:
    def bark(self):
        print("Dog barking")

#The child class tommy inherits class dog and animals

class Tommy:
    def eat(Animal,Dog):
        print("Tommy eating meat...")

#issubclass
print(issubclass(Tommy,Dog))
print(issubclass(Tommy,Animal))
print(issubclass(Dog,Animal))

#isinstance
t = Tommy()
d = Dog()
print(isinstance(t, Tommy))
print(isinstance(t, Dog))
print(isinstance(t,Animal))
print(isinstance(d,Animal))