# Canvas and Drawing
# Echo

# Text output can be used with strings to put the results 
#   of functions on the canvas rather than in the box to 
#   the right. Here is a simple echo program to show that
#   in action. Note that it can only display the parts of
#   messages that fit in the canvas.

import simplegui
import math

# Global Variables

canvas_width = 800
canvas_height = 100
message = ""

# Event Handlers

def echo(text):
    global message
    message = text
        
def draw(canvas):
    canvas.draw_text(message, (50, 60), 20, "Lime")

# Frame

frame = simplegui.create_frame("Pictures", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.add_input("Echo", echo, 100)

# Remember to start the frame
frame.start()