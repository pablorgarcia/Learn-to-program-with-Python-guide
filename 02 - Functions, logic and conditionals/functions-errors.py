# Functions - take an input(s) and return an output
# Errors


# Indentation must be 4 spaces. Note that different types of
#   errors occur if the issue is under-indentation rather than
#   over-indented.

def f():
    x = 2
#  x += 1
#     x += 2
    print x

# Indentation 4 spaces too shallow cause errors on subsequent 
#   indented lines.
    
def f():
    x = 2
#x = 4
    print x
    
# If you forget to put parenthesis when calling a function,
#   errors don't always appear. That is because the program
#   treats the function name as a variable name instead.

def fun():
    print "Fun!"
fun
print "Ex. 1:", fun

# Functions should not have the same name as a global variable.
#   This overrides the deletes the original variable's value.
#   Assigning a new value to the variable eliminates the 
#   function.

name = 5
print "Ex. 3:", name
def name():
    return 4
print "Ex. 2:", name
print "Ex. 3:", name()
name = 9
print "Ex. 4:", name
#print "Error", name()

# Functions can however have the same name as a local variable

def first():
    x = 10
    return x
def x():
    x = 11
    return x
print "Ex. 5:", first()
print "Ex. 6:", x()


# Errors can also appear if a function name is misspelled

def function():
    return "hi"
#print funtion()


# If a function expects a certain number of parameters, 
#   attempting to call it with a different number will cause
#   an error.

def echo(num):
    return num
def add(num_1, num_2):
    return num_1 + num_2
#echo(4, 5)
#echo()
#add(2)

# You also need to be careful that the types of parameters
#   that you are giving to your function matches the types
#   of parameters it expects. Also notice that this returns
#   an error in the function rather than the function call.
#add(2, "b")


# The command 'return' also throws an error if it is not
#   inside of a function
#return "hi"


# Functions with no ':' also have errors
#def something()


# Note: If two functions have the same name, the second will
#   override the first.
def a():
    return 1
def a():
    return 2
print "Ex. 8:", a()



