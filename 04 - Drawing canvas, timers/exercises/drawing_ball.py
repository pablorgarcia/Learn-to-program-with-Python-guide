""" Complete the program template below and add two buttons
that control the radius of a white ball centered in the middle
of the canvas. Clicking the 'Increase radius' button should increase
the radius of the ball. Clicking the 'Decrease radius' button
should decrease the radius of the ball, except that the ball radius
should always be positive. """

import simplegui


# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    canvas.draw_circle([WIDTH // 2, HEIGHT // 2], ball_radius, 1, 'White', 'White')

# Event handler for buttons
def increase_radius():
    global ball_radius
    ball_radius += RADIUS_INCREMENT

def decrease_radius():
    global ball_radius
    if ball_radius > RADIUS_INCREMENT:
        ball_radius -= RADIUS_INCREMENT


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame('Ball control', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button('Increase radius', increase_radius)
frame.add_button('Decrease radius', decrease_radius)


# Start the frame animation
frame.start()
