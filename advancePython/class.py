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
# Parent Clsss
class Person1:
  def __init__(self, fname, lname, age):
    self.firstname = fname
    self.lastname = lname
    self.age = age

  def printName(self):
    print(self.firstname, self.lastname, self.age)

#Use the Person1 class to create an object, and then execute the printname method:
x = Person1("John", "Doe", 90)
x.printName()
"""
class Patient(Person1):
   def __init__(self, fname, lname, age, gender):
      Person1.__init__(fname, lname, age)
      self.gender = gender
      # this code gives error here
    def printGender(self):
        print("Patient's gender is"+ self.gender)

patientObject = Patient("amazon", "aws", 48, "M")
patientObject.printName()
patientObject.printGender()
"""

class Patient(Person1):
   def __init__(self, fname, lname, age, gender):
      super().__init__(fname, lname, age)
      self.gender = gender

newPatient = Patient("John", "Doe", 79, "M")
newPatient.printName()

# Multiple Inheritance
class BaseFunc1:
   def baseFuncSample1(self):
    print("This is the first base function")

class BaseFunc2:
   def baseFuncSample2(self):
      print("This is the second base function")

class MultiInheritanceSample(BaseFunc1, BaseFunc2):
   pass

multiInheritanceObject = MultiInheritanceSample()
multiInheritanceObject.baseFuncSample1()
multiInheritanceObject.baseFuncSample2()

print(multiInheritanceObject.__class__.__bases__)

# Multiple Level Inheritance
class Level1:
   def level1Sample(self):
      print("This is level 1 sample")

class Level2(Level1):
   def level2Sample(self):
      print("This is level 2 sample")

class MultipleLevelInheritance(Level2):
   pass

multiLevelInheritanceObject = MultipleLevelInheritance()
multiLevelInheritanceObject.level1Sample()
multiLevelInheritanceObject.level2Sample()
