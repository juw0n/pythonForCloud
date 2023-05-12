# A function is a block of code that run only when it is called.

# Defining a function
def myHelloWorld():
    print("This is my Hello World! Function")

# calling a function
myHelloWorld()

# Defining a function with arguement
def greeting(name):
    print("Hello "+ name)
greeting("Juwon")

# Defining a function with arbitrary arguement (Unknow number of arg)
def selectItem(*item):
    print("The second item is: " + item[1])
selectItem("FF10", "Twilight", "Lord of the Rings")

# Defining a function with named arbitrary arguement (Unknow number of arg)
def selectKnownItem(**item):
    print("The requested item is: " + item["mov3"])
selectKnownItem(mov1= "FF10", mov2= "Twilight", mov3= "Lord of the Rings", mov4= "Gladiator")

#  using return statement in function definition
def sum(a,b):
    return a + b
totalSum = sum(20, 60)
print("The total sum of this function is: ", totalSum)


