# To create a module just save the code you want in a file with the file extension .py:

# Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)

# Now we can use the module we just created, by using the import statement:

# Example
# Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")

# : When using a function from a module, use the syntax: module_name.function_name.

# Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule

a = mymodule.person1["age"]
print(a)

# You can create an alias when you import a module, by using the as keyword:
# Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)

# There are several built-in modules in Python, which you can import whenever you like.

# Import and use the platform module:

import platform

x = platform.system()
print(x)

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function
# 
# :

import platform

x = dir(platform)
print(x)

# You can choose to import only parts from a module, by using the from keyword.

# Example
# The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])
# When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

