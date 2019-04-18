#multilevel inheritance
class Animal:
    def speak(self):
        print("Animal speaking")
#The child class dog inherits the base class Animal

class Dog(Animal):
    def bark(self):
        print("Dog barking")
#The child class tommy inheitance another child class Dog
class Tommy(Dog):
    def eat(self):
        print("Tommy eating bread..")

d = Tommy()
d.eat()
d.bark()
d.speak()