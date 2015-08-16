""" Given the following program template,
add draw commands to the draw handler to draw "This is easy?"
on the canvas. The precise size
and location of the text on the canvas is not important. """

import simplegui

# Draw handler
def draw(canvas):
    canvas.draw_text('This is easy?',[100, 112], 48, 'Red')


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame('This is easy', 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()