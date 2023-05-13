"""
A class is like a blueprint for creating object in python
An Object is an instantiation of a class. it is a collection of variable and functions that act on the provided data defined in the class.
"""
# class definition
class mySimpleClass:
    x = 40
    def printValue(self):
        print("The value of x is:", self.x)

# creating an object from the class
c = mySimpleClass()
# calling a method from the class
c.printValue()

# Constructor Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greetPerson(self):
        print("Hello "+ self.name)
        print("You are", self.age, "years old")
        
p = Person("Esther", 98)
p.greetPerson()

# Python Inheritance
