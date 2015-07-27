# Functions - take an input(s) and return an output
# Structure


# Functions have two parts: a header and a body. The header
#   of a function is made up of the keyword 'def' followed by
#   the function name, parameters in parenthesis, and a colon.
#   The body is indented 4 spaces after the header.

def function_name(parameters):
    print "This is the body!!!"
    
# Functions can have 0 or more parameters.

def no_parameters():
    print "The parenthesis were empty this time!!!"
    
def more_parameters(a, b, c):
    print "There are three parameters now!!!"

# Functions can have multiple lines in the body as well.
    
def more_lines():
    print "This function is longer."
    print "It has multiple lines."
    print "Three, to be exact."
    
  
# If you try to run the program, you will see that nothing
#   is printed to the screen. The lines inside the body of
#   a function are not used by the computer until the
#   function is called.

# These are function calls. Try them out by uncommenting them.
#no_parameters()
#more_lines()

# If there are parameters in the method header, the call
#   must also have parameters in the parenthesis.
#function_name(1)
#more_parameters(1, 2, 3)


# The word 'pass' can be used in the body of a function to
#   cause the function to do nothing. This can be useful
#   when you know you will need a function, but are not 
#   quite sure how you want it to work.

def pointless_function():
    pass

pointless_function()

# Another special word is 'return'. If you place the word
#   'return' followed by some value, the function will
#   return that value. Nothing after the return statement
#   is executed.

def returning_function():
    print "Ex. 1: First"
    return 4
    print "Second"

# Uncomment these to try it for yourself.
#x = returning_function()
#print "Ex. 2:", x

# Function names have the same limitations as variable
#   names. As a reminder: valid names consist of 
#   letters, numbers, and / or underscores (_), 
#   and start with a letter or underscore. They should also
#   be descriptive, and not change color.

# Good names
def add_two(x):
    pass
def print_strings(s_one, s_two, s_three):
    pass
def multiply_by_4(x):
    pass

# Bad names (commented ones produce errors)
def a_t(x):
    pass
def prstr(o, t, th):
    pass
def m4(x):
    pass
def i_hate_comp_sci():
    pass
#def -a(a):
#    pass
#def x&y(x, y):
#    pass
#def 4ever():
#    pass
#def print(x):
#    pass
#def True(x):
#    pass

# These two re-define pre-existing functions, which is not
#   a very good idea. Don't do it, please. 
def max(x, y):
    pass
def int(x):
    pass