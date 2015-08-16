# Motion
# Ball Track


# This is a simple game to see how many times the user can 
# guide a ball around a track using the arrow keys to 
# control the ball's velocity. If you would like an added
# challenge, you can try to improve the code to time and 
# display the user's fastest lap.
# Note: Using global variables is very useful when you would
# like to change aspects of your program. Because ball_radius
# and the track radii are global variables and all of the 
# necessary calculations were done based on these variables,
# you can change the track width or ball size to increase
# or decrease the difficulty of the game.

import simplegui
import math

# Global Variables

canvas_width = 600
canvas_height = 600
# Although the variables are initially empty, I call the
# reset() function before starting the frame to initialize
# them so they are not empty when the program runs.
ball_pos = []
ball_vel = []
ball_radius = 20
inner_track_radius = 150
outer_track_radius = 280
num_laps = 0
high_score = 0
# Checks to see if the ball has gone at least halfway around
# the track before counting a lap to prevent cheating.
over_half = False

# Helper Functions

# Returns the distance between two points
def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Event Handlers
        
def draw(canvas):
    # Remember globals!
    global over_half, num_laps, high_score
    mid = [canvas_width / 2, canvas_height / 2]
    
    # Track
    canvas.draw_circle(mid, outer_track_radius, 1, 'Aqua', 'Black')
    canvas.draw_circle(mid, inner_track_radius, 1, 'Aqua', 'Green')
    
    # Start and halfway lines
    canvas.draw_line((mid[0], mid[1] - inner_track_radius), (mid[0], mid[1] - outer_track_radius), 5, 'White')
    canvas.draw_line((mid[0], mid[1] + inner_track_radius), (mid[0], mid[1] + outer_track_radius), 1, 'White')
    
    # Ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    canvas.draw_circle(ball_pos, ball_radius, 1, 'Red', 'Red')
    
    # Score
    canvas.draw_text('Laps:', [260, 230], 30, 'Aqua')
    # Note that the num_laps and high_score must be converted into strings
    canvas.draw_text(str(num_laps), [290, 280], 30, 'Aqua')
    canvas.draw_text('High Score:', [210, 340], 30, 'Aqua')
    canvas.draw_text(str(high_score), [290, 390], 30, 'Aqua')
    
    # Hit sides and crossed lines
    # If the ball is inside the inner circle or outside the outer circle
    if distance(ball_pos, mid) > outer_track_radius - ball_radius or distance(ball_pos, mid) < inner_track_radius + ball_radius:
        reset()
    # Elif the ball is touching the line on the top half of the circle
    elif over_half and abs(ball_pos[0] - mid[0]) < ball_radius and ball_pos[1] < mid[1]:
        over_half = False
        num_laps += 1
        if num_laps > high_score:
            high_score = num_laps
    # Elif the ball is touching the line on the bottom half of the circle
    elif abs(ball_pos[0] - mid[0]) < ball_radius and ball_pos[1] > mid[1]:
        over_half = True

def reset():
    global ball_pos, ball_vel, num_laps, over_half
    ball_pos = [canvas_width / 2, canvas_height / 2 - (outer_track_radius + inner_track_radius) / 2]
    ball_vel = [0, 0]
    num_laps = 0
    over_half = False
    
def keydown_handler(key):
    acc = 1
    # Notice that because we are only changing the elements 
    # of the list ball_vel the keyword global is not necessary.
    if key==simplegui.KEY_MAP['left']:
        ball_vel[0] -= acc
    elif key==simplegui.KEY_MAP['right']:
        ball_vel[0] += acc
    elif key==simplegui.KEY_MAP['down']:
        ball_vel[1] += acc
    elif key==simplegui.KEY_MAP['up']:
        ball_vel[1] -= acc
    
# Frame and Timer

frame = simplegui.create_frame('Ball Track', canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_canvas_background('Green')
frame.add_button('Reset', reset)

# Start
reset()
frame.start()