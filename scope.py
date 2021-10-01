# A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()

# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
# Example
# The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.

def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Also, use the global keyword if you want to make a change to a global variable inside a function.

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)