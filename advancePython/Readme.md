"""
Global Variable are varialbe created in the main body of python code and outside any function. These type of variable are said to have global score. that is they can be used anywhere in the code. a function can become global function by using the Keyword 'global'

Local Variable are variable created within a function. they are said to have local scope. that is only available within the function

Any varialbe that is neither local or global is cal nonLocal variable. they are used in nested function. 

Documentation: Docstring
Documentation string or docstring is used to describe what a function does.

Anonymous/Lambda Dunction:
These are function that doesn't have a define name. they are define using the 'lambda' keyword and a lambda function can take any number of arguement, but can only have one expression.

Recursive Function:
A function that can call another function. but in python, a function can call itself. they are called recursive function. 

Nested Function
A function defined inside another function is called nested function.

Closures
These are nested/inner functions that are enclosed within thr outer function. they can access variable present in the uter function scope. it can access thse variable even after the outer function has complte execution

Decorator
A decorator is  design pattern in python that allows us to add a new functionality to an existing function without modifying it's structure. it act as a wrapper

Python classes
One of the popular approaches of prgramming is by creating object, E as much as possible. this is also known as DRY(Don't Repaet Yourself)
A class is like a blueprint for creating object in python
An Object is an instantiation of a class. it is a collection of variable and functions that act on the provided data defined in the class. NOTE: whenever an object calls its method, the object itself passed as the first arguement

The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
  pass

Constructors in Python
class functions that begin with double underscore __ are special functions, out of which thae most used one is __init__() function. All classes that have a function call __init__(), which is always executed when the class is being initiated are called Constructor function.
Note: The __init__() function is called automatically every time the class is being used to create a new object.

Class Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

Super Function
The super() function in python allow the child class to inherit all the method and properties from the parent. there will be no need to use the name of the parent, it will automatically inherit the methof and properties from the parent

Multiple Inheritance
If a class derived from more thank one base/parent class, that clsaa is called multiple inheritance

Multiple Level Inheritance
In python a class can inherit from a derived class, it's called multi-level inheritance.

Python Packages
While Python modules may contain several classes, functions, variables, etc. Python packages contain several modules. In simpler terms, Package in Python is a folder that contains various modules as files and a file with the name __init__.py.

It is a directory with python files and a file with the name __init__.py(this file is always blank/empty). This means evry directory inside a python path, which contains a file named __init__.py(this file is always blank/empty) will be treated as a package by python.
A python package can have sib-packages and modules. it's a well-organised hierarchy of directory for easier access.

File Handling in Python
A file is a named location (object) on a disk to store information/data. A file is used to store data permanently on a no-volatile memory such as hard drive(HDD)/solid state drive(SSD) etc.
File handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files.
File Handling
The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and mode.
Where the following mode is supported:
r: Reda =>open an existing file for a read operation.
w: Write => open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
a: Append => open an existing file for append operation. It won’t override existing data.
x - Create - Creates the specified file, returns an error if the file exists
r+: Read and Write => To read and write data into the file. The previous data in the file will be overridden.
w+: Write and Read => To write and read data. It will override existing data.
a+: Append and Read => To append and read data from the file. It won’t override existing data.
In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

Python Directories
Python has an inbuilt os module which provides us with many useful method/function to work with directories, sub-directories and files as well.

Python and JSON
JSOn is a human-readale lightweight data-interchanging format. It is a syntax for storing and exchanging data. JSON is text, written with JavaScript object notation and is used in transmitting data in web applications.

JSON values can only be one of the following 6 data type (string, number, object, arrays, boolean, null)

Python has a built-in package call json which can be used to work with JSON data.

You can convert Python objects of the following types, into JSON strings:

1. dict
2. list
3. tuple
4. string
5. int
6. float
7. True
8. False
9. None

Python Requests Module
Using the Request module, you can Make a request to a web page, and print the response text.
The requests module allows you to send HTTP requests using Python.
The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

Install the request module using python3 -m pip install requests

The Request module support the following method: 
delete(url, args)	=> Sends a DELETE request to the specified url
get(url, params, args) => Sends a GET request to the specified url
head(url, args)	=> Sends a HEAD request to the specified url
patch(url, data, args)	Sends a PATCH request to the specified url
post(url, data, json, args)	=> Sends a POST request to the specified url
put(url, data, args)	=> Sends a PUT request to the specified url
request(method, url, args)	=> Sends a request of the specified method to the specified url.

Virtual Environment
A virtual environment is python is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. which means Different applications can then use different virtual environments.
The module used to create and manage virtual environments is called venv.

How to create Virtual Environment.
1. Make a directory(project directory) and cd into the directory
*** mkdir projectVirtual
*** cd projectVirtual
2. create the virtual environment using the venv module "myVirtualEnv" is the name of the virtual environment
** python3 -m venv myVirtualEnv
3. Next we activate the virtual environment
** source myVirtualEnv/bin/activate
or 
** . myVirtualEnv/bin/activate

"""