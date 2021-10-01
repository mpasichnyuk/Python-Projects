# Create a class named MyClass, with a property named x:
class MyClass:
  x = 5

# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

# All classes have a function called __init__(), which is always executed when the class is being initiated.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Insert a function that prints a greeting, and execute it on the p1 object:
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sayname(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.sayname()

# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Set the age of p1 to 40:

p1.age = 40

# Delete the age property from the p1 object:

del p1.age

# Delete the p1 object:

del p1

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
# Example
class Person:
  pass

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Create a class named Student, which will inherit the properties and methods from the Person class
# Use the pass keyword when you do not want to add any other properties or methods to the class.

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

# Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function. The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

