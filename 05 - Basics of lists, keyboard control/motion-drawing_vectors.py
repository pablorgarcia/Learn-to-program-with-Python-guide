# Collisions and Reflections
# Drawing Vectors


# This program draws a vector from point_one to point_two,
#   which are given by the user, and displays the magnitude
#   (length) of the vector rounded to two decimal places.

import simplegui
import math

# Global Variables

canvas_width = 400
canvas_height = 400
point_one = [canvas_width // 2, canvas_height // 2]
point_two = [canvas_width // 2, canvas_height // 2]
magnitude = 0
angle = 0

# Helper Functions

def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# This is just for the pretty arrow at the end of the vector,
#   so don't worry about the math
def get_angle(pos1, pos2):
    if pos1[0] == pos2[0]:
        if pos2[1] - pos1[1] > 0:
            return math.pi / 2
        else:
            return math.pi * 3 / 2
    angle = math.atan((pos1[1] - pos2[1]) / (pos1[0] - pos2[0]))
    if pos2[0] - pos1[0] < 0:
        angle += math.pi
    return angle
    
# Event Handlers
        
def draw(canvas):
    canvas.draw_line(point_one, point_two, 1, 'White')
    
    # Draws an arrow at the end of the vector. Don't worry
    #   about the math, this is just to make the program 
    #   look nice.
    if magnitude > 0:
        pos = (point_two[0] - 8 * math.cos(angle), point_two[1] - 8 * math.sin(angle))
        a = (math.pi * 2 / 3) * 0 + angle
        p1 = [pos[0] + math.cos(a) * 20 / 3, pos[1] + math.sin(a) * 20 / 3]
        a = (math.pi * 2 / 3) * 1 + angle
        p2 = [pos[0] + math.cos(a) * 20 / 3, pos[1] + math.sin(a) * 20 / 3]
        a = (math.pi * 2 / 3) * 2 + angle
        p3 = [pos[0] + math.cos(a) * 20 / 3, pos[1] + math.sin(a) * 20 / 3]
        canvas.draw_polygon([p1, p2, p3], 1, 'White', 'White')
    
    canvas.draw_text('Magnitude of Vector: ' + str(round(magnitude, 2)), (50, 30), 20, 'Red')
    
def update_x1(text):
    # Note that I don't have to list point_one as a global
    global magnitude, angle
    if text.isdigit() and int(text) <= canvas_width:
        point_one[0] = int(text)
        magnitude = distance(point_one, point_two)
        angle = get_angle(point_one, point_two)
    else:
        print 'Invalid input'
        
def update_y1(text):
    global magnitude, angle
    if text.isdigit() and int(text) <= canvas_height:
        point_one[1] = int(text)
        magnitude = distance(point_one, point_two)
        angle = get_angle(point_one, point_two)
    else:
        print 'Invalid input'

def update_x2(text):
    global magnitude, angle
    if text.isdigit() and int(text) <= canvas_width:
        point_two[0] = int(text)
        magnitude = distance(point_one, point_two)
        angle = get_angle(point_one, point_two)
    else:
        print 'Invalid input'

def update_y2(text):
    global magnitude, angle
    if text.isdigit() and int(text) <= canvas_height:
        point_two[1] = int(text)
        magnitude = distance(point_one, point_two)
        angle = get_angle(point_one, point_two)
    else:
        print 'Invalid input'

# Frame and Timer

frame = simplegui.create_frame('Drawing Lines', canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(draw)
# Note that input points must be on the canvas.
frame.add_input('x1', update_x1, 50)
frame.add_input('y1', update_y1, 50)
frame.add_input('x2', update_x2, 50)
frame.add_input('y2', update_y2, 50)

# Start
frame.start()