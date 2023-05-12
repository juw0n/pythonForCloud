"""
Python program terminate as soon as it encouter errors, to prevent this exception handling is used. in Python, exception is handled using try..except..statement
"""
# Simple Error Handling
try:
    print(x)
except:
    print("An exception Occurred")

# Multiple Error Handling
try:
    print(f)
except NameError:
    print("Variable is not defined")
except:
    print("Something else when wrong")

# Error handling with else keyword
try:
    print("Hello")
except NameError:
    print("Something else when wrong")
else:
    print("Nothing when wrong")

# Error handling with finally keyword
print("Almost there")
try:
    print(Oops)
except NameError:
    print("Something when wrong")
finally:
    print("The 'try except' is finished")

