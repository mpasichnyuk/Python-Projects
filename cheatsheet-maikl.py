firstName = input("enter your first name: ")
lastName = input("input your last name:")

print("Hello, ", firstName, lastName)
# this is a comment, don't read me.
"""
this is a string
it is a multistring
you can use it as a multiline comment
you also can assign it to a variable
"""

# this is called CASTING like typecasting in Hollywood
x = str(3)  # assign var with type string, result is '3'
y = int(4)  # will asssign the number four to Y, integer
z = float(5)  # will assign the value of 5.0 , float type

print(type(x))  # will give us the type of var, like strm float, intenger

maikl = 1
Maikl = 2
# two different vars, CAPS are important!
# vars should start with _ or with letter, not number!
# no hyphens- in vars, only _underscore

x, y, z = "One", "Two", "Three"

a = b = c = "Orange"

fruitsList = ["Apple", "Orange", "Banana"]
x, y, z = fruitsList  # will assign each var a seprate value

def myFunc()
    x = 'Fantastic'
    global y # will declare a global var y
    print('Python is' + x)


xlist = ['one', 'two','three']
ytuple = ('five', 'six', 'seven')

r = range(6) #range type

objdict = {"Name": "Maikl","age": 36}

setVar = {"banana", "orange", "apple"}

x = 5
x = float(x)
# converts x from int type to float type

x = 35e3 #scientific notaton meaning TO THE POWER OF 10X3

import random
print(random.randrange(1,10))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#yhistime its not a comment, python will parse this code since you declare a var
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1]) # will give you e

for x in "banana":
  print(x) 
# will print each char on a new line if you use IN

a = 'Hello world'
b = len(a)
print(b)

txt = "The best things in life are free!"
print("free" in txt) #true

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt) #returns True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5]) #will start with 2nd char and end with 4th. not taking the 5th!
print(b[2:6])
print(b[:6]) #slice from beginning
print(b[2:]) #slice to the end

#begin from the end
b = "Hello, World!"
print(b[-5:-2]) #will give the orl from the World!

a = "Hello, World!"
print(a.upper()) # to UPPERCASE

a = "Hello, World!"
print(a.lower())

a = "    Hello, World!    "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))
# Jello, World!

a = "Hello, World!"
print(a.split(",")) # returns list ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# .format method will insert values in strings where placeholders {} are
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# using placeholder will give us 
#My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#we can use number to specify order of placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# forward slash is / - it is going higher, as should all we do
# backslahs is going down. dont be balckslash \
# but we can use it as an escape charcter!!
txt = "We are the so-called \"Vikings\" from the north."

# string method can help you findm replace, analyze, capitale srings, etc
#All string methods returns new values. They do not change the original string.

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# these are all False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")



x = 15
y = 2
print(x // y)
#the floor division // rounds the result down to the nearest whole number

x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# start fron the -end, print last item with
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# will change the 1st and 2nd indexed items in array

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ['apple', 'watermelon']  

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
# ['apple', 'banana', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #remove the index 1 item, or if pop() will remove last item

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()

# LOOPS

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# ['apple', 'banana', 'mango']

# newlist = [expression for item in iterable if condition == True]

newlist = [x.upper() for x in fruits] 
# will uppercase item before appending to new list

newlist = [x if x != "banana" else "orange" for x in fruits]
# "Return the item if it is not banana, if it is banana return orange".

# sorting lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# by default UPPERCASE will bsorted first, even if it is Z
# we can override this

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

list2 = list1
# will create only refernece to the same memory space of list1
# if list1 will be changed, so will list2
# we can override this

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits # red will be a list will all other items - array
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

