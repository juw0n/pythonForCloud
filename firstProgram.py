# first program
import keyword

print("Hello world!")
print("The list of Python keywords is : ")
print(keyword.kwlist)

print("\nThe list of Python Data Type is : ")
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
print("Type check in python: ")
name="Oluwajuwon"
age=109
print(type(name))
print(type(age))

print("Sequence Types:")
list=["Juwon", "Sang", "Song", 4, 5, 6, 0.3, 0.9 ]
print(list, list[2], list[1:3])
print(type(list))
print(type(list[2]))
print(type(list[5]))
print(type(list[6]))
print(list[-1])
list.insert(65, "newValue")
print(list)

tuple=(4, 5, 6, "Juwon", "Sang", "Song")
print("This sequence is unchangeable", tuple)
print(type(tuple))

set={"a", "b", "c", 9, 8, 7 }
print("This sequence is unordered, unchangeable,:", set)
print(type(set))
