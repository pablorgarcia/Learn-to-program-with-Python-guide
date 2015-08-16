""" Create a circle in the center of the canvas.
Use a timer to increase its radius one pixel every tenth of a second."""

import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def tick():
    global radius
    radius += 1
    
# Draw handler
def draw(canvas):
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], radius, 1, 'White', 'White') 
        
# Create frame and timer
frame = simplegui.create_frame('Expanding circle', 200, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# Start timer
frame.start()
timer.start()
