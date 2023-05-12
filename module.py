"""
A module in python is a file containing Python functions, statement and definition, just like a code library.
Type of Moudle is Python
1. Syetm Module: they are available built-in modules in python. they are utilize and importing the module name using import statement.

2. Custom Module: These module are use to break down large program into snall manageable and organised file that provides reuseability of codes.

"""

import platform
n = platform.system()
print(n)

# example of custome module useage
print("\nExample of custom module usage")
import customModule
customModule.greet("Oluwajuwon")

# custom module alias example
print("\nExample of custom module alias usage")
import customModule as cm
print(cm.greet("Oluwakemi"))
print(cm.person["height"])

# Using dir() function to get all the variable and function in a module
import customModule
g = dir(customModule)
print(g)