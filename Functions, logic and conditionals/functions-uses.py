# Functions - take an input(s) and return an output
# Uses


# The main purpose of a function is to do something that 
#   needs to be done multiple times. This saves you the 
#   need to code the same statements over and over in your
#   programs.

my_age = 30
his_age = 35

def print_ages():
    print "Ages:", my_age, his_age

print_ages()
my_age += 1
print_ages()
his_age += 22
print_ages()
print

# Functions frequently use parameters to obtain information
#   from the regular program, then perform operations on the
#   given info. Parameters can be object, including numbers,
#   strings, and booleans.
    
x = 3

def add_two(num):
    num += 2
    print num
    
add_two(x)
print

message = "Hello awesome people!"

def print_message(s):
    print s
    print "Bonus Line !!! :D"
    
print_message(message)
print

# This usually does not change the original variable.
print "x:",  x
print "message:", message
  
    
print "--------"
# If you would like to use a function to make a computation
#   or do something else, but you do not want to print the
#   outcome to the screen until later, you can use a return
#   statement.

num1 = 3
num2 = 5
num3 = 6

def add_nums(a, b, c):
    answer = a + b + c
    return answer

num4 = add_nums(num1, num2, num3)
print "Num 4:", num4


def multiply_nums(a, b):
    answer = a * b
    return answer

num4 = multiply_nums(num1, num4)
print "New Num4:", num4

# Return statements can return expressions, and print
#   statements can directly print out the returned values
#   of functions. This can save you from having to make too
#   many unnecessary variables.

def divide_nums(a, b):
    return a / b

print "Num 5:", divide_nums(num4, num1)


print "--------"
# Be careful when attempting to print the value of a function
#   with no return statement.

def new_function():
    pass

def new_function_2():
    a = 8
    
print "Test 1:", new_function()
print "Test 2:", new_function_2()

# The same thing happens with variables

word = new_function()
print "Word:", word
print

# Things can get weird when you attempt to print a function
#   that already has print statements.

def other_new_function():
    print "HELLO"
    
print "Start", other_new_function(), "Stop"

# What happened was: the computer printed "Start", then
#   called the method other_new_function() which printed 
#   "HELLO" and started a new line, then attempted to print
#   the value returned by other_new_function() (there wasn't
#   one), and finally printed off the "Stop" at the end of
#   the statement.

