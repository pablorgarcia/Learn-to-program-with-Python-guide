# Keyboard Input
# Shape Selection


# This is a simple program that allows you to change the 
# size, color, fill, and shape of an image on the screen.

import simplegui

# Global Variables

canvas_width = 200
canvas_height = 200
size = 100
colors = ['DeepPink', 'Red', 'DarkOrange', 'Yellow', 'Lime', 'Green', 'Blue', 'Aqua', 'Purple', 'Magenta']
fill = False
shapes = ['Square', 'Circle', 'Triangle']
color_index = len(colors) // 2
shape_index = len(shapes) // 2

# Event Handlers
        
def draw(canvas):
    if shapes[shape_index] == 'Square':
        x = canvas_width / 2 - size / 2
        y = canvas_height / 2 - size / 2
        if fill:
            canvas.draw_polygon([(x, y), (x + size, y), (x + size, y + size), (x, y + size)], 5, colors[color_index], colors[color_index])
        else:
            canvas.draw_polygon([(x, y), (x + size, y), (x + size, y + size), (x, y + size)], 5, colors[color_index])
    elif shapes[shape_index] == 'Circle':
        if fill:
            canvas.draw_circle([canvas_width / 2, canvas_height / 2], size / 2, 5, colors[color_index], colors[color_index])
        else:
            canvas.draw_circle([canvas_width / 2, canvas_height / 2], size / 2, 5, colors[color_index])
    elif shapes[shape_index] == 'Triangle':
        x = canvas_width / 2 - size / 2
        y = canvas_height / 2 - size / 2
        if fill:
            canvas.draw_polygon([(x, y + size), (x + size, y + size), (x + size / 2, y)], 5, colors[color_index], colors[color_index])
        else:
            canvas.draw_polygon([(x, y + size), (x + size, y + size), (x + size / 2, y)], 5, colors[color_index])
    
def key_handler(key):
    # REMEMBER TO STATE YOUR GLOBAL VARIABLES. Comment out the
    # line below for one example of things that can go wrong.
    global fill, size, color_index, shape_index
    if key == simplegui.KEY_MAP['f']:
        fill = not fill
    elif key == simplegui.KEY_MAP['s']:
        if shape_index > 0:
            shape_index -= 1
    elif key == simplegui.KEY_MAP['d']:
        if shape_index < len(shapes) - 1:
            shape_index += 1
    elif key == simplegui.KEY_MAP['z']:
        if size > 10:
            size -= 10
    elif key == simplegui.KEY_MAP['x']:
        if size < 200:
            size += 10
    elif key == simplegui.KEY_MAP['c']:
        if color_index > 0:
            color_index -= 1
    elif key == simplegui.KEY_MAP['v']:
        if color_index < len(colors) - 1:
            color_index += 1

# Frame and Timer

frame = simplegui.create_frame('Shape Selection', canvas_width, canvas_height) 
# This statement is necessary to declare a function to be the
# keydown handler. Try changing the line that is commented
# out to see the difference between a keyup handler and a 
# keydown handler.
frame.set_keydown_handler(key_handler)
#frame.set_keyup_handler(key_handler)
frame.add_label('Shape: s and d')
frame.add_label('Fill: f')
frame.add_label('Size: z and x')
frame.add_label('Color: c and v')

# Register Event Handlers

frame.set_draw_handler(draw)

# Start
frame.start()