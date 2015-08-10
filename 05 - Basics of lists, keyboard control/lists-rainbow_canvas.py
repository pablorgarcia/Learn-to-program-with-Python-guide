# Lists
# Rainbow Canvas


"""This is an example of cycling through a list to change the
color of the canvas. Try changing the timer interval to
see what happens."""

import simplegui

# Global Variables

canvas_width = 300
canvas_height = 300
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
# Different rainbow colors list (uncomment to use)
# colors = ['DeepPink', 'Red', 'DarkOrange', 'Yellow', 'Lime', 'Aqua', 'Magenta']
index = 0

# Event Handlers
        
def draw(canvas):
    frame.set_canvas_background(colors[index])
    
def next_color():
    global index
    index += 1
    """Using modulus ensures that you will never go to an 
    invalid index, and also causes the cycle to repeat
    again from the first color when it reaches the end
    of the list."""
    index = index % len(colors)

# Frame and Timer

frame = simplegui.create_frame('Rainbow Canvas', canvas_width, canvas_height) 
timer = simplegui.create_timer(500, next_color)

# Register Event Handlers

frame.set_draw_handler(draw)

# Start
frame.start()
timer.start()