#the print() function is used to output data to the console. It can take multiple arguments and will print them separated by a space by default. You can also specify a different separator using the sep parameter.

# print ('hello world')

'''python indentation
if 5>2:
   print('five is greater than two')
else:
    print("true")'''

#python variables
#x = 'Good morning'
#y = 'Asantewaa'
#print(x, y)


#statements
#print("Hello World!")
#print("Have a good day.")
#print("Learning Python is fun!")

#NB: Python uses indentation to define blocks of code. Indentation is important in Python and is used to indicate a block of code. The standard indentation is 4 spaces.
#Best practice: Put each statement on its own line so your code is easy to understand.

#print("Hello World,", end=" ")
#print("Have a good day.")
#print("Learning Python is fun!")

#print(40*5)
""" this is a multi-line comment
that spans multiple lines
print("My name is Asantewaa and I am learning Python programming language.", "I am " + str(20) + " years old.") """


#Variables are containers for storing data values. In Python, you don't need to declare the type of a variable; it is determined automatically based on the value assigned to it. You can assign values to variables using the assignment operator (=).

# casting is used to specify the data type of a variable. For example, if you want to convert a string to an integer, you can use the int() function. Similarly, you can use float() to convert a string to a floating-point number.

"""x = int(5)  # x will be 5
y = float(3.14)  # y will be 3.14
print(x *y)"""

"""type() function is used to determine the data type of a variable. For example, if you want to check the data type of a variable, you can use the type() function.
x = 5
y = "Asantewaa"
print(type(x))
print(type(y))"""


"""String variables can be declared either by using single or double quotes:
x = "Asantewaa"
y = 'Asantewaa'
print(x)
print(y)"""

#NB variable names must start with a letter or an underscore, and can only contain letters, numbers, and underscores. Variable names are case-sensitive, which means that "myVariable" and "myvariable" are considered different variables.

"""
camelCase is a naming convention where the first letter of each word is capitalized except for the first word. For example, "myVariableName" is in camelCase. This convention is commonly used in programming languages like JavaScript and Java.

#PascalCase is a naming convention where the first letter of each word is capitalized, including the first word. For example, "MyVariableName" is in PascalCase. This convention is commonly used in programming languages like C# and .NET.

#snake_case is a naming convention where words are separated by underscores, and all letters are lowercase. For example, "my_variable_name" is in snake_case. This convention is commonly used in programming languages like Python.
"""

"""x, y, z = "Guava", "Tiger", 20
print(x)
print(y, z)

x = y = z = "Mango"
print(x)
print(y)
print(z)"""

"""
Letters = ["J", "E", "S", "U", "S"]
x,y,z,a,b = Letters
print(x,y,z,a,b)....this is called unpacking a list"""

#x = "Asantewaa "
#y = "is interning at DigiCoast"
#z = "and she is enjoying the experience."
#print(x, y, z)
#print(x + y +z)

#global variables are variables that are defined outside of a function and can be accessed from anywhere in the code. Local variables, on the other hand, are variables that are defined inside a function and can only be accessed within that function.

'''x = "Global variable"
def my_function():
    print(x)  # This will print the global variable
my_function()  # Output: Global variable

x = "Global variable"
def my_function():
    x = "Local variable"
    print(x)  # This will print the local variable
my_function()  # Output: Local variable
#print(x)  # Output: Global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)'''

#use the global keyword to modify a global variable inside a function. If you want to change the value of a global variable inside a function, you need to use the global keyword to indicate that you are referring to the global variable.

'''def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

x = 5
y = "Asantewaa"
print(type(x))

x = 5
y = 3.14
z = "Hello"
a = 1j
print(type(x))
print(type(y))
print(type(z))
print(type(a))'''



'''x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))'''


#random variables
#import random
#print(random.randrange(1, 10))

'''x = int(1)   # x will be 1
a = float(x)
b = str(x)
print(a)
print(b)

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')'''

#strings are arrays of bytes representing unicode characters. In Python, strings are immutable, which means that once a string is created, it cannot be changed. You can create a string by enclosing characters in either single quotes (' ') or double quotes (" ").

#a = "Hello, World!"
#print(a[5])  # This will print the sixth character of the string
#for loop is used to iterate over a sequence (such as a list, tuple, string, etc.) and execute a block of code for each item in the sequence. The syntax of a for loop in Python is as follows:
#for x in "banana":
   # print(x)

#a = "Hello, World!"
#print(len(a))

#txt = "Hello, World!"
#print("free" in txt)  # This will return True if "free" is found in the string, otherwise it will return False

#txt = "Hello World!"
#if "Hello" in txt:
    #print("Yes, 'Hello' is present.")   


#slicing is a technique used to extract a portion of a string. In Python, you can use slicing to get a substring from a string. The syntax for slicing is as follows:
#string[start:end:step]

#a = "The digicoast"
#print(a[2:5])

#upper() method is used to convert a string to uppercase. It returns a new string with all characters in uppercase.
#a = "sugar"
#print(a.upper())

#lower() method returns the string in lower case.
#b = "SUGAR"
#print(b.lower())

#strip() method removes any leading and trailing whitespace from the string. It returns a new string with the whitespace removed.
#c = "   Hello, World!   "
#print(c.strip())

# the replace() method replaces a specified phrase with another specified phrase. It returns a new string with the replacements made.
#d = "Hello, World!"
#print(d.replace("H", "J"))

# The split() method splits a string into a list where each word is a list item. It returns a list of the words in the string, separated by the specified separator (default is any whitespace).
#e = "Hello, World!"
#print(e.split(","))

#to concatenate two or more strings, you can use the + operator. This will join the strings together into a single string.
'''f = "Hello"        
g = "World"
h = f + " " + g
print(h)'''

#f-strings, also known as formatted string literals, are a way to embed expressions inside string literals, using curly braces {}. They were introduced in Python 3.6 and provide a more concise and readable way to format strings.
'''age = 36
txt = f"My name is John, I am {age}"
print(txt)'''


#boolean values are a data type that can only have two possible values: True or False. They are often used in conditional statements and loops to control the flow of a program based on certain conditions.
'''x = 5
y = 10
print(x > y)  # This will print False because 5 is not greater than 10
print(x < y)  # This will print True because 5 is less than 10'''

'''a = 10
b = 20
if a<b:
    print("True")
else:
    print("false")
'''    
#the elif keyword is used in conditional statements to check multiple conditions. It stands for "else if" and allows you to specify additional conditions to check if the previous conditions were not met.
'''a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")


score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:   
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

a = 100
b = 878
if b>a:
    print("b is greater than a")
elif a>b:
    print("a is greater than b")
else:
    print("a is not greater than b")


a = 5
b = 10
c = 59
if a<b and c==a:
    print("Both conditions are true")
elif a<b or c==a:
    print("At least one of the conditions is true")
else:   
    print("Neither condition is true")

age = 20
is_student = True
has_id = False

if age >=18 and is_student and has_id:
        print("You are eligible for a student discount.")   
else:
        print("You are not eligible for a student discount.")'''


#when combining multiple conditions in an if statement, you can use the logical operators "and", "or", and "not" to create more complex conditions. The "and" operator returns True if both conditions are true, the "or" operator returns True if at least one condition is true, and the "not" operator negates a condition, returning True if the condition is false and False if the condition is true.

#when combining multiple logical operators in a single if statement, you can use parentheses to group conditions and control the order of evaluation. This is important because logical operators have different precedence levels, and using parentheses can help ensure that your conditions are evaluated in the way you intend.

'''temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")
In this example, the condition checks if the temperature is greater than 20 and it is not raining, or if it is the weekend. The parentheses ensure that the "not is_raining" condition is evaluated correctly in conjunction with the "temperature > 20" condition before applying the "or" operator with "is_weekend".'''


#nested if statements are if statements that are contained within another if statement. They allow you to check multiple conditions in a hierarchical manner. The syntax for nested if statements is as follows:

'''name = "Alice"
age = 30
has_id = True
if name == "Alice":
    if age >= 18:
      if has_id:
        print("Alice is an adult.")
    else:
        print("Alice is a minor.")'''

userName = "Sandra"
password = "Sandy#56"
is_Active = True        