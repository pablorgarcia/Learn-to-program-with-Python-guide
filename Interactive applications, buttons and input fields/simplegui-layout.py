# SimpleGUI
# Layout


# For this program, just run it. Don't worry about the code,
#   we haven't learned how to use it yet. Make sure you can
#   identify all of the parts and what they are used for.
#   Note that the status area will only update if you click
#   inside of the canvas.





































# Fine. Look at the code then. I'm not explaining it yet
#   though.
# I suppose you can learn from messing around with it and 
#   changing things if you are that dedicated.

import simplegui

width = 400
height = 300

def keydown_handler(key):
    pass
def keyup_handler(key):
    pass
def click(pos):
    pass
def button_handler():
    pass
def input_handler(x):
    pass
def draw_handler(canvas):
    canvas.draw_text("This is the canvas!", [6, 40], 40, "White")
    canvas.draw_text("This area can display shapes, images, and text.", [6,100], 15, "White")
    canvas.draw_circle([110,200], 50, 10, "Blue", "blue")
    canvas.draw_text("TEXT", [250,200], 30, "Red")
    
frame = simplegui.create_frame("Window Name", width, height)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.set_mouseclick_handler(click)
frame.add_label("This is the control area!")
frame.add_label("This is where buttons and input fields go! (and obviously text can go here too)")
frame.add_button("Button", button_handler)
frame.add_input("Input field:", input_handler, 50)
frame.add_label(" ")
frame.add_label("The status area gives information about key presses and mouse clicks. Try it out!")
frame.add_label("Status area:")

frame.start()











