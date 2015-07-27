# SimpleGUI
# Errors


# The first error occurs if you forget to import simplegui

#frame = simplegui.create_frame("Test", 300, 200)

import simplegui

# An error also occurs if you forget to create a frame before
#   attempting to call methods on it.

#frame.start()
#frame.set_canvas_color("White")

# Leave the following line uncommented for the rest of the 
#   program. Note that since the frame has not been started,
#   the canvas displays as white rather than black. This is 
#   a clue that you forget to start your frame.

frame = simplegui.create_frame("Test", 300, 200)

# Frame creation requires specific parameters

int_num = 300
float_num = 200.75
num = 100
string = "Hello"

# These two are fine:
#frame = simplegui.create_frame(string, int_num, float_num)
#frame = simplegui.create_frame(string, float_num, int_num, num)

# These are not:
#frame = simplegui.create_frame(num, num, num)
#frame = simplegui.create_frame(string, num, num, string)
#frame = simplegui.create_frame(string, string, string)
#frame = simplegui.create_frame(string, num)
#frame = simplegui.create_frame(string, num, num, num, num)

# Misspelling methods also doesn't help. Neither does
#   forgetting parenthesis, even if it doesn't throw an error.

#frame = simplegui.createframe(string, num, num)
#frame.set_background("White")
#frame.set_background
# Not an error, but causes issues anyway. Don't do it.
frame.start

# Misspelling color strings or making them up throws errors
#   as well. Uncomment the last line of code to see them
#   in action.

# These two are fine (note: capitalization does not matter):
#frame.set_canvas_background("red")
#frame.set_canvas_background("ReD")

# These are not:
#frame.set_canvas_color("reed")
#frame.set_canvas_color("R3D")
#frame.set_canvas_color(True)
# Pink is not supported. Check the documentation for the 
#   full list.
#frame.set_canvas_color("pink")

#frame.start()




