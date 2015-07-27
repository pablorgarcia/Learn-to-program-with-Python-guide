# Buttons
# Canvas Color


# This is a sample program that allows the user to change the
#   color of the canvas using buttons.

import simplegui

# Global Variables

canvas_color = "Black"  # by default, the canvas is black
canvas_width = 300
canvas_height = 300

# Helper Functions

def change_canvas():
    frame.set_canvas_background(canvas_color)

# Event Handlers

def to_red():
    global canvas_color
    canvas_color = "Red"
    change_canvas()

def to_yellow():
    global canvas_color
    canvas_color = "Yellow"
    change_canvas()

def to_green():
    global canvas_color
    canvas_color = "Green"
    change_canvas()
    
def to_blue():
    global canvas_color
    canvas_color = "Blue"
    change_canvas()
    
def to_black():
    global canvas_color
    canvas_color = "Black"
    change_canvas()
    
def to_white():
    global canvas_color
    canvas_color = "White"
    change_canvas()

# Frame

frame = simplegui.create_frame("Colors!", canvas_width, canvas_height) 

# Register Event Handlers

frame.add_button("Red", to_red, 60)
frame.add_button("Yellow", to_yellow, 60)
frame.add_button("Green", to_green, 60)
frame.add_button("Blue", to_blue, 60)
frame.add_button("Black", to_black, 60)
frame.add_button("White", to_white, 60)

# Start Frame

frame.start()