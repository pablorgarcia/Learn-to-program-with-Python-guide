# Input Fields
# Structure


# Input fields allow the user to give data to the program.
#   Input fields pass data that is typed into the control
#   area to designated event handlers in the program. It is
#   important to note that this information is always given
#   as a string.
# To use input fields, you must import simplegui and create a
#   frame. Comment out the lines below to see what kind of 
#   error you get if your forget this step. Than uncomment 
#   them again so you can actually run the rest of the program.

import simplegui
frame = simplegui.create_frame("Input Fields", 300, 500)

# Input fields require a name and a handler. Unlike buttons, 
#   input fields must also have a width. The handler is a 
#   method with exactly one parameter.

width = 50
def input_handler(string_input):
    pass

inp = frame.add_input("Name", input_handler, width)


# The button handler can be any function a single string 
#   parameter. Note that you must hit the enter key after
#   typing input to actually give the computer your data and
#   call the event handler.

def echo(string):
    print string
    
inp = frame.add_input("Echo", echo, 50)

# You get an error if you try to create the button before you
#   define the event handler, or if you use a handler with
#   the wrong number or type of parameters. Note that errors
#   with the parameters of the handlers only show up when
#   you try to enter input while the program is running.

#inp_error = frame.add_input("Error :(", e_handler, 50)

def e_handler(string):
    pass

# Even though the variable is called string, it is treated
#   like a number in the function.
def wrong_handler(string):
    string += 5

def other_handler(a, b):
    pass

inp_error = frame.add_input("Error :(", wrong_handler, 100)
inp_error = frame.add_input("Other Error :(", other_handler, 100)

# Input fields don't actually need to be assigned to a variable
#   to work.

def generic_handler(s):
    pass

frame.add_input("No Variable!", generic_handler, 100)

# Input fields appear on the screen in the order they were 
#   created.

inp_b = frame.add_input("Second", generic_handler, 50)
inp_a = frame.add_input("First", generic_handler, 50)

# As usual, errors can occur if you misspell things...

#fram.add_input("Error", generic_handler, 50)
#frame.add_inputz("Error", generic_handler, 50)
#frame.add_input("Error", generc_handler, 50)

# ...and if you give incorrect parameters.

#frame.add_input("Error", generic_handler)
#frame.add_input("Error", generic_handler, "50")
#frame.add_input("Error")
#frame.add_input(100, generic_handler, "Error")
#frame.add_input("Error", generic_handler, 50, 50)

frame.start()