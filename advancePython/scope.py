# global Scope
d = "I am a Global Vaiable"
def someFunc():
    print(d + " inside a function")
someFunc()

print(d + " outside a function")

# global variable using global keyword
def somefunc1():
    global x 
    x= 200
    print("x inside function is:",x)
somefunc1()
print("x outside function is:",x)

# Local varialbe and scope
def someFunc2():
    g= 400
    print("g inside function is:",g)
someFunc2()
# print("g inside function is:", g)

# Non loacal variable and scope
def outterFunc():
    z = "I am a Local Value"
    def innerFunc():
        nonlocal z #the nonlocal keyword change the valie of z
        z = "I am  non-local value"
        print("z inner function value is:",z)
    innerFunc()
    print("z Outer function value is:",z)
outterFunc()
