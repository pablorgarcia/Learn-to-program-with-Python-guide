# Interactive Drawing
# Hidden Picture

# Just one more fun example of drawing on the canvas :)
# See if you can figure out what the picture is!

import simplegui
import math

# Global Variables
canvas_width = 600
canvas_height = 600
yellow = False
navy = False
blue = False
black = False
white = False
teal = False

# Event Handlers
def toggle_yellow():
    global yellow
    yellow = not yellow
    
def toggle_navy():
    global navy
    navy = not navy
    
def toggle_blue():
    global blue
    blue = not blue
    
def toggle_black():
    global black
    black = not black
    
def toggle_white():
    global white
    white = not white
    
def toggle_teal():
    global teal
    teal = not teal
        
def draw(canvas):
    if yellow:
        canvas.draw_line((230, 530), (200, 540), 3, 'Yellow')
        canvas.draw_line((230, 530), (210, 550), 3, 'Yellow')
        canvas.draw_line((230, 530), (220, 555), 3, 'Yellow')
        canvas.draw_line((370, 530), (400, 540), 3, 'Yellow')
        canvas.draw_line((370, 530), (390, 550), 3, 'Yellow')
        canvas.draw_line((370, 530), (380, 555), 3, 'Yellow')
        
    if navy:
        canvas.draw_polygon([(220, 140), (270, 110), (225, 80)], 1, 'Navy', 'Navy')
        canvas.draw_polygon([(380, 140), (330, 110), (375, 80)], 1, 'Navy', 'Navy')
        canvas.draw_circle((100, 340), 40, 1, 'Navy', 'Navy')
        canvas.draw_circle((90, 380), 40, 1, 'Navy', 'Navy')
        canvas.draw_circle((100, 420), 40, 1, 'Navy', 'Navy')
        canvas.draw_polygon([(120, 305), (120, 455), (300, 400), (300, 360)], 1, 'Navy', 'Navy')
        canvas.draw_circle((500, 340), 40, 1, 'Navy', 'Navy')
        canvas.draw_circle((510, 380), 40, 1, 'Navy', 'Navy')
        canvas.draw_circle((500, 420), 40, 1, 'Navy', 'Navy')
        canvas.draw_polygon([(480, 305), (480, 455), (300, 400), (300, 360)], 1, 'Navy', 'Navy')
    
    if blue:
        canvas.draw_circle((300, 400), 150, 1, 'Blue', 'Blue')
        canvas.draw_circle((300, 200), 100, 1, 'Blue', 'Blue')
   
    if white:
        canvas.draw_circle((250, 180), 30, 1, 'White', 'White')
        canvas.draw_circle((350, 180), 30, 1, 'White', 'White')
        
    if black:
        canvas.draw_circle((250, 195), 15, 1, 'Black', 'Black')
        canvas.draw_circle((350, 195), 15, 1, 'Black', 'Black')
      
    if yellow:
        canvas.draw_polygon([(280, 220), (320, 220), (300, 270)], 1, 'Yellow', 'Yellow')
        
    if teal:
        canvas.draw_circle((300, 400), 100, 1, 'Teal', 'Teal')

# Frame
frame = simplegui.create_frame('Shapes', canvas_width, canvas_height) 

# Register Event Handlers
frame.set_draw_handler(draw)
frame.add_button('Yellow', toggle_yellow, 60)
frame.add_button('Navy', toggle_navy, 60)
frame.add_button('Blue', toggle_blue, 60)
frame.add_button('Black', toggle_black, 60)
frame.add_button('White', toggle_white, 60)
frame.add_button('Teal', toggle_teal, 60)

# Remember to start the frame
frame.start()