# Canvas and Drawing
# Structure

# The draw handler allows the user to draw things on the 
#   canvas. Make sure you read all the way to the end of the
#   program to find out how to register a function as the
#   draw handler.

import simplegui

# The draw method is a type of event handler. It takes 
#   exactly one parameter, commonly called the canvas. The
#   canvas can be passed as a parameter to other methods, 
#   if needed.
        
def draw(canvas):
    # The draw handler runs about 60 times each second.
    # Uncomment the next line to see.
    #print "hi"
    
    # Text can also be drawn on the canvas using the 
    #   draw_text() method of the canvas.
    message = "It alive! It alive!"
    point = (50, 100) # The point is the lower left-hand corner of the text
    text_size = 20
    color = "Lime"
    canvas.draw_text(message, point, text_size, color)
    canvas.draw_text('How are you today?', (150, 200), 30, "Magenta")
    
    # Notice that the first coordinate of the point gets bigger
    #   as you go to the right, and the second coordinate of
    #   the point gets bigger as you go down.
    canvas.draw_text("Hi", (25, 225), 20, "Red")
    canvas.draw_text("Hola", (75, 225), 20, "Blue")
    canvas.draw_text("Oi", (25, 275), 20, "Yellow")
    canvas.draw_text("Bonjour", (75, 275), 20, "Green")
    
    # Text can also go off the screen
    canvas.draw_text("You are so nice!      Omg she's so annoying...", (300, 50), 20, "Silver")
    
def other_handler(canvas):
    canvas.draw_text("Yay! You found me!", (100, 170), 20, "Aqua")
    
def wrong_handler():
    pass

# Frame

frame = simplegui.create_frame("Draw", 500, 300) 

# Register Event Handlers

# This is how to register the draw handler. Uncomment the
#   one below it to try a different draw handler.
frame.set_draw_handler(draw)
#frame.set_draw_handler(other_handler)
# An error will occur if you assign the draw handler to
#   a function with the wrong parameters
#frame.set_draw_handler(wrong_handler)

# Remember to start the frame!
frame.start()