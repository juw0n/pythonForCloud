# implicit Type Conversion
n1 = 987
n2 = 2.78
nSum1 = n1 + n2
print("n1 is of type:",type(n1))
print("n2 is of type:", type(n2))
print(nSum1)
print("nSum1 is of type:", type(nSum1))

# explicit Type Conversion
n8 = 123
n9 = "456"
print("\nDatatype of n8:", type(n8))
print("Datatype of n9:", type(n9))
nSum2 = n8 + int(n9)
print(nSum2)
print("Datatype of nSum2:", type(nSum2))

# Dynamic TypeConversion
n5 = input("\nPlease enter a number n5: ")
n6 = input("Please enter another number n6: ")
print("Datatype of n5:", type(n5))
print("Datatype of n6:", type(n6))
nSum3 = n5 + n6
print("n5 + n6:", nSum3)
print("Datatype of nSum3:", type(nSum3))
print("The input from user is usually in string datatype")
print("\nAfter Dynamic conversion:")
nSum3 = float(n5) + float(n6)
print("n5 + n6:", nSum3)
print("New Datatype of nSum3:", type(nSum3))