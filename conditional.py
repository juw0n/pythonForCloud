# This is a conditional Statement script
age= int(input("How old are you? \n"))
if age < 2:
    print("You are an Infant")
elif age < 5:
    print("You are a Toddler")
elif age < 13:
    print("You are a Child")
elif age < 20:
    print("You are a Teenager")
elif age < 40:
    print("You are a Adult")
elif age <= 59:
    print("You are a Mid Age Adult")
else:
    print("You are a Senior Adult")
