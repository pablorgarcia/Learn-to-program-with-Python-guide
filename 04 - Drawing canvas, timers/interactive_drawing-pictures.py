# Interactive Drawing
# Pictures

# This program allows the user to display pictures created
# using the canvas. Note the order of commands in the draw
# method; if you change them, does the image change?
# Note: I am definitely not an artist. I promise I tried.
# Feel free to change the pictures. (if you do that, it
# may be easier to work if you temporarily set the 
# global variables to True)

import simplegui
import math

# Global Variables
canvas_width = 600
canvas_height = 600
fish = False
house = False
flower = False
big_dipper = False

# Event Handlers
def toggle_fish():
    global fish
    fish = not fish
    
def toggle_house():
    global house
    house = not house
    
def toggle_flower():
    global flower
    flower = not flower
    
def toggle_big_dipper():
    global big_dipper
    big_dipper = not big_dipper
        
def draw(canvas):
    if fish:
        # Body
        canvas.draw_circle((450, 100), 40, 2, 'Orange', 'Orange')
        # Eye
        canvas.draw_circle((430, 100), 10, 2, 'Black', 'White')
        canvas.draw_circle((426, 104), 5, 1, 'Black', 'Black')
        # Tail
        a = 470
        b = 100
        w = 80
        canvas.draw_polygon([(a, b), (a + w / 2 / math.tan(math.pi / 6), b - w / 2), (a + w / 2 / math.tan(math.pi / 6), b + w / 2)], 2, 'Orange', 'Orange')
    if flower:
        # Leaf
        canvas.draw_circle((140, 500), 30, 2, 'Maroon', 'Green')
        # Stem
        w = 30
        h = 150
        canvas.draw_polygon([(100, 400), (100, 400 + h), (100 + w, 400 + h), (100 + w, 400)], 2, 'Maroon', 'Green')
        # Petals
        canvas.draw_circle((115, 420), 40, 4, 'Black', 'White')
        canvas.draw_circle((115, 320), 40, 4, 'Black', 'White')
        canvas.draw_circle((165, 370), 40, 4, 'Black', 'White')
        canvas.draw_circle((65, 370), 40, 4, 'Black', 'White')
        # Center
        canvas.draw_circle((115, 370), 35, 2, 'Black', 'Yellow')
    if house:
        # Structure
        canvas.draw_polygon([(300, 400), (550, 400), (550, 550), (300, 550)], 2, 'Silver', 'Silver')
        canvas.draw_polygon([(275, 400), (425, 300), (575, 400)], 2, 'Maroon', 'Maroon')
        # Door
        canvas.draw_polygon([(400, 475), (400, 550), (450, 550), (450, 475)], 2, 'Red', 'Red')
        canvas.draw_circle((410, 512), 5, 2, 'Black', 'Black')
        # Windows
        canvas.draw_polygon([(325, 450), (325, 500), (375, 500), (375, 450)], 4, 'Black', 'Blue')
        canvas.draw_polygon([(525, 450), (525, 500), (475, 500), (475, 450)], 4, 'Black', 'Blue')
    if big_dipper:
        # Lines
        canvas.draw_polyline([(50, 70), (100, 60), (150, 72), (190, 90), (210, 150), (275, 160), (300, 107)], 2, 'White')
        # Stars
        canvas.draw_circle((50, 70), 5, 1, 'White')
        canvas.draw_circle((100, 60), 5, 1, 'White')
        canvas.draw_circle((150, 72), 5, 1, 'White')
        canvas.draw_circle((190, 90), 5, 1, 'White')
        canvas.draw_circle((210, 150), 5, 1, 'White')
        canvas.draw_circle((275, 160), 5, 1, 'White')
        canvas.draw_circle((300, 107), 5, 1, 'White')

# Frame

frame = simplegui.create_frame('Pictures', canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
frame.add_button('Fish', toggle_fish, 100)
frame.add_button('House', toggle_house, 100)
frame.add_button('Flower', toggle_flower, 100)
frame.add_button('Big Dipper', toggle_big_dipper, 100)

# Remember to start the frame
frame.start()