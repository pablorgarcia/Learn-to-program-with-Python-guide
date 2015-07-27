# Buttons
# Structure


# Buttons allow the user to control the flow of a program.
#   Button presses call methods in the program.
# To use buttons, you must import simplegui and create a frame.
#   Comment out the lines below to see what kind of error you
#   get if your forget this step. Than uncomment them again
#   so you can actually run the rest of the program.

import simplegui
frame = simplegui.create_frame("Buttons", 300, 300)

# Buttons require a name and a handler. The handler is a 
#   method with no parameters.

def button_handler():
    pass

button_one = frame.add_button("Name", button_handler)


# The button handler can be any function without parameters.

def print_hi():
    print "HI"
    
button_two = frame.add_button("'HI' button", print_hi)

# You get an error if you try to create the button before you
#   define the event handler, or if you use a handler with
#   parameters. Note that the second doesn't actually give
#   you the error until you try to click the button.

#button_error = frame.add_button("Error button :(", e_handler)

def e_handler():
    pass

def other_handler(x):
    pass

button_error = frame.add_button("Error button :(", other_handler)

# Buttons also have an optional parameter that controls their
#   width. This is useful for making columns of buttons that
#   are even.

def generic_handler():
    pass

button_three = frame.add_button("Three", generic_handler, 150)
button_four = frame.add_button("Four", generic_handler, 150)

# Buttons are created by add_button whether or not you assign
#   the result to a variable.

frame.add_button("No Variable!", generic_handler)

# Buttons appear on the screen in the order they were created.

button_b = frame.add_button("B", generic_handler)
button_a = frame.add_button("A", generic_handler)

# As usual, errors can occur if you misspell things...

#fram.add_button("Error", generic_handler)
#frame.add_a_button("Error", generic_handler)
#frame.add_Button("Error", generic_handler)
#frame.add_button("Error", generc_handler)

# ...and if you give incorrect parameters.

#frame.add_button("Error", generic_handler, "50")
#frame.add_button("Error")
#frame.add_button(100, generic_handler, "Error")
#frame.add_button("Error", generic_handler, 50, 50)

# Note that if you set a width to a button with too much
#   text, the text will get cut off but no error will occur.

#frame.add_button("Alphabetic", generic_handler, 50)

# As a final note, event handlers can still be called by
#   something other than the button. Uncomment the function
#   call to see for yourself.

def output():
    print "Hello. What a lovely day."
    
frame.add_button("Output", output)
#output()

frame.start()