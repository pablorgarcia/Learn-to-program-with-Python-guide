import simplegui

# Buggy code -- doesn't start frame

message = 'Welcome!'

def click():
    """Change message on mouse click."""
    global message
    message = 'it\'s alive! it\'s alive!'

def draw(canvas):
    """Draw message."""
    canvas.draw_text(message, [50, 118], 36, 'Red')

# Create a frame and assign callbacks to event handlers

frame = simplegui.create_frame('Home', 300, 200)
frame.add_button('Click me', click)
frame.set_draw_handler(draw)


# Buggy code -- doesn't start timers

def timer1_handler():
    print '1'
    
def timer2_handler():
    print '2'

simplegui.create_timer(100, timer1_handler)
simplegui.create_timer(300, timer2_handler)
