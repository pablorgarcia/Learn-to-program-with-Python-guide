#--------------------Value Errors -------------------#

################### Example 1 ########################
#ValueError: invalid literal for int() with base 10: ' '
#Cause: trying to convert something to an integer
#that doesn't represent an integer

#To generate this error, run the program and put a
#letter, punctuation, space, etc. in the input field


import simplegui

def input_guess(guess):
    print int(guess)
    text_field.set_text("")


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Value Error #1", 300, 200)
text_field = frame.add_input("Put a non-digit character here and press enter: ", input_guess, 100)

# Start the frame animation
frame.start()

#This program will function correctly if you enter a 
#digit in the text box, and error out otherwise. That's
#because while digits can be represented as integers,
#other characters, like a, b, c, etc., cannot*. When 
#Python tries to convert 'a' into an integer, it finds
#that there is no associated value for it, and errors out.
#This error could have been generated in just one line,
#but I wanted to put it in a format that was more like 
#what you would see in the mini project (namely, GTN).


#Ok, so other characters can and are represented as integers.
#It's called ASCII, and each character has a corresponding
#integer value. However, int() does not take that value
#into account, so we still get an error. 
