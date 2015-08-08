# Timers
# Reaction Time

# This program tests your reaction in milliseconds using a timer.
# Notice the uses of start() and stop() methods.

import simplegui
import random

# Global Variables
canvas_width = 200
canvas_height = 200
reaction_time = 0
# Used to see if the circle should be drawn
started = False
count = 0

# Event Handlers
def check_start():
    global started, count
    count += 1
    # This makes sure that the circle won't be drawn for at
    # least one second after starting the frame or clicking
    # the restart button.
    if count > 10:
        # This increases the likelihood of starting and ensures
        # that the game will start within a time limit.
        if count / 500.0 > random.random():
            started = True
            reaction_timer.start()
            circle_timer.stop()

def increment():
    global reaction_time
    reaction_time += 1
    
def stop_button():
    if started:
        reaction_timer.stop()
        print 'Your reaction time was', reaction_time, 'milliseconds'
        
def draw(canvas):
    if started:
        canvas.draw_circle([canvas_width / 2, canvas_height / 2], 60, 2, 'Red', 'Red')
        
def restart():
    global started, count, reaction_time
    started = False
    count = 0
    reaction_time = 0
    circle_timer.start()
    

# Frame

frame = simplegui.create_frame('Reaction Time', canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)

# By the way, these are labels. You can check the docs for
# more info.
label = frame.add_label('Get ready...')
frame.add_label('Press \'stop\' when the red circle appears.')
                        
frame.add_button('Stop', stop_button, 75)
frame.add_button('Restart', restart, 75)

# Note that the timers do not have the same name or purpose
circle_timer = simplegui.create_timer(100, check_start)
reaction_timer = simplegui.create_timer(1, increment)

# Start Frame and circle_timer
frame.start()
circle_timer.start()