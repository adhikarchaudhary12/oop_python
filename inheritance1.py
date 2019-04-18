class Animal:
    def speak(self):
        print("Animal speaking")
#child class dog inherits the base class Animal

class Dog(Animal):
    def bark(self):
        print("Dog barking")


d = Dog()
d.bark()
d.speak()