#--------------------Type Errors -------------------#

################### Example 5 ########################
#TypeError: handler must be a function
#Cause: trying to register an event handler that doesn't
#exist. Could be caused by a typo, or by leaving 
#parentheses in the function name.


import simplegui, random

# Handler for mouse click
def click():
    print "It works now!"


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Type Error #5", 300, 200)
frame.add_button("Click me", click())

# Start the frame animation
frame.start()


#When you register an event handler, you must put in the
#name of an already-existing function. You may not pass
#in any parameters to an event handler (that means that
#your event handler can't be something like random.randrange,
#which requires parameters to work). This error is also
#commonly caused by leaving the parentheses in the
#function name, as above. To fix this particular error, 
#just take out the parentheses after 'click' in line
#19.
