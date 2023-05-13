# Docstring
def greet(name):
    """
        This function greet someon whose name is enter when the function is called.
    """
    print("Hello, " +name)
greet("Esther")

# normal function
def doSum1(a,b):
    return a + b
ans=doSum1(3,5) 
print(ans)


# Anonymous function
doSum = lambda a,b: a + b
print(doSum(40, 60))

myList= [0,1,2,3,4,5,6,7,8,9]
filterList = list(filter(lambda x:(x>4), myList))
print(filterList)

myList1 = [0,1,2,3,4,5,6,7,8,9]
filterList1 = list(map(lambda x:(x+x), myList1))
print(filterList1)


# Recursive Function
def factoriaCal(z):
    if z == 1:
        return 1
    else:
        return (z * factoriaCal(z-1))
num = 4 

k = factoriaCal(num)
print("The factoria of ", num, "is 1*2*3*4 =", k)

# Nested Function
def greet(name):
    def greetFirstName():
        # This is the nested function
        print("Hello!", name)
    greetFirstName()
greet("Ariel")

# Closures function
def hello(q):
    def helloFirst():
        # nested funcion 
        print("Hi, how are you", q)
    return helloFirst

printHelloFirst = hello("Araoluwa")
printHelloFirst()
