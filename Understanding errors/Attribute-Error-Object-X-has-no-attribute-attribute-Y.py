#------------------Attribute Errors ------------------#

################### Example 1 ########################
#AttributeError: 'Frame' object has no attribute 'make_draw_handler'
#Cause: A frame object doesn't have the method "make_draw_handler"


import simplegui

def draw(canvas):
    #don't do anything in the draw handler. 
    pass 

#create the frame
frame = simplegui.create_frame("AttributeErrorTest", 100, 100)

#set your handlers
frame.make_draw_handler(draw)

#start the frame
frame.start()


#When you see one of these errors, look for a call like this:
#
# thing_before_dot.thing_after_dot()
#
#An AttributeError like this means that the thing before
#the dot doesn't recognize the thing after the dot. In this
#case, a Frame doesn't recognize the call "make_draw_handler". 
#That's because the method name is really "set_draw_handler". 
#Change "make" to "set" in the example above, and the error
#will disappear.

