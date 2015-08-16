# Control ball position with the arrow keys

import simplegui

# initialize state
width = 300
height = 300
position = [int(width/2), int(height/2)]
radius = 15
velocity = 5

# event handlers
def keydown(key):
    if key == simplegui.KEY_MAP['down']:
        position[1] = position[1] + velocity
    elif key == simplegui.KEY_MAP['up']:
        position[1] = position[1] - velocity
    elif key == simplegui.KEY_MAP['right']:
        position[0] = position[0] + velocity
    elif key == simplegui.KEY_MAP['left']:
        position[0] = position[0] - velocity

def draw(canvas):
    canvas.draw_circle(position, radius, 2, 'red', 'red')

# create frame
frame = simplegui.create_frame('Key Handling', width, height)

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# start frame
frame.start()
