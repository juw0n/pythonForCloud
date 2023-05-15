# importing module from package
import Greeting.Person.greet
Greeting.Person.greet.sayHi()

# importing packages as alias
import Greeting.Person.greet as greet_user
greet_user.sayHi()

# importing module without package prefix
from Greeting.Person import greet
greet.sayHi()

# importing only function from package module
from Greeting.Person.greet import sayHi
sayHi()