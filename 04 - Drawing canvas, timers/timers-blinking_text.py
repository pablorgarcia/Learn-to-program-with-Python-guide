# Timers
# Blinking Text

# In this program, the user's text blinks every time
# the timer handler is called. Try changing the timer frequency
# to see what happens. Notice that if the text is too
# long not all of it will be shown. For an added challenge,
# can you come up with a way to solve that issue?

import simplegui

# Global Variables
canvas_width = 600
canvas_height = 100
message = 'Burger Bar!'
displayed = True
timer_interval = 1000 # In milliseconds (1000 ms = 1 s)

# Event Handlers
def input_handler(text):
    global message
    message = text

# Switches whether or not the text is visible    
# Note that it does not have any parameters
def timer_handler():
    global displayed
    displayed = not displayed

def draw(canvas):
    if displayed:
        canvas.draw_text(message, [10, 65], 30, 'Aqua')

# Frame
frame = simplegui.create_frame('Blinking Text', canvas_width, canvas_height) 

# Register Event Handlers
frame.set_draw_handler(draw)
frame.add_input('Your message:', input_handler, 100)

# Creates a timer. Check the docs for more details.
timer = simplegui.create_timer(timer_interval, timer_handler)

# Remember to start the timer as well as the frame
frame.start()
timer.start()