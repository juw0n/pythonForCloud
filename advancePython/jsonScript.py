import json
# some JSON:
person_json =  '{ "name":"John Deo", "age":30, "city":"Lagos, Nigeria"}'
# parse person_json(converting JSON to python data type):
person_python = json.loads(person_json)
# the result is a Python dictionary:
print("The person city is: ", person_python["city"])

# Convert from Python to JSON
# you can convert python into a JSON string by using the json.dumps() method.
# a Python object (dict):
x = {
  "name": "John",
  "age": 35,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

person_python["age"] = 69
newPersonJSON = json.dumps(person_python)
print(newPersonJSON)

# Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))