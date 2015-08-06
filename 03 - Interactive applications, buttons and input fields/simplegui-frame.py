# SimpleGUI
# Frame


# Frames are the basic outline of the user interface. Frames
#   are created using the syntax below. Remember to import
#   simplegui first.
# Note: Since CodeSkulptor can currently support only one 
#   frame, you will need to comment out the frame-creation
#   lines as you go.

import simplegui

#frame = simplegui.create_frame("New Frame", 200, 300)

# Here are the parts of the frame:
window_name = "New Frame"
canvas_width = 200
canvas_height = 300

#frame = simplegui.create_frame(window_name, canvas_width, canvas_height)

# Another example with new values
window_name = "New Name"
canvas_width = 600
canvas_height = 100

#frame = simplegui.create_frame(window_name, canvas_width, canvas_height)

# There is also an optional fourth parameter for the frame
window_name = "New Frame"
canvas_width = 400
canvas_height = 300
control_width = 400

#frame = simplegui.create_frame(window_name, canvas_width, canvas_height)
#frame = simplegui.create_frame(window_name, canvas_width, canvas_height, control_width)

# Note that the first value is the width, while the second
#   value is the height. THIS IS IMPORTANT :)

#frame = simplegui.create_frame("Test", 400, 200)
#frame = simplegui.create_frame("Test", 200, 400)

# For the next example, please uncomment the following frame

#frame = simplegui.create_frame("Test", 300, 200)

# You can also change the color of the canvas.

#frame.set_canvas_background("Red")
#frame.set_canvas_background("Blue")
#frame.set_canvas_background("White")

# There are more color strings that you can use. Check the 
#   documentation for more info.

# The final part of the frame is starting it. The following
#   method must be called for the canvas to be drawn correctly.
#   Try commenting it out to see what changes.

frame.start()


