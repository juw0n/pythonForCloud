person = {
    "name": "Juwon",
    "age": 109,
    "height": 6.7
}
print("This is a key-value pair dictionary: ", person)
print(type(person))
print(person["age"])
print(person["height"])
print(type(person["age"]))
print(type(person["name"]))
print(type(person["height"]))

#get value of a dictionary by key
print(person["name"])

# Change value of a key in dictionary
person["age"]= 121
print(person["age"])
person.update({"age": 126})
print(person["age"])

# adding a new value to a dictionary
person["shoe_size"]=42
print("This is a key-value pair dictionary: ", person)

# deleting a particular key from dictionary
person.pop("height")
print(person)
del person["shoe_size"]
print(person)

# To empty a dictionary
person.clear()
print(person)