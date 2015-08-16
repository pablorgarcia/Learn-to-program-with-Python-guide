""" Use a timer to toggle the canvas background back
and forth between red and blue every 3 seconds.
Locate the appropriate call to change
the background color of the canvas."""

import simplegui 

color = 'Red'


# Timer handler
def tick():
    global color
    if color == 'Red':
        color = 'Blue'
    else:
        color = 'Red'
    frame.set_canvas_background(color)
        
# Create frame and timer
frame = simplegui.create_frame('Counter with buttons', 200, 200)
frame.set_canvas_background(color)
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()
