# Lists
# Digital Numbers


"""This program displays two-digit whole numbers in a manner 
similar to a digital clock. What happens if you hit the
decrease button when the number is 0? Why? Where in the
code does that take place?"""

import simplegui

# Global Variables

canvas_width = 150
canvas_height = 150
num = 0

# Helper Functions

def draw_num(canvas, num, x, y):
    # x and y are the top left hand coordinates of the number
    lights = [False, False, False, False, False, False, False]
    
    """There are a total of 6 'lights' or shapes that can be
    'on' (drawn) or 'off' (not drawn). This if-elif 
    segment decides which ones should be 'on' (True) 
    based on the number given to the function."""
    if num == 0:
        lights = [True, True, True, False, True, True, True]
    elif num == 1:
        lights = [False, False, True, False, False, False, True]
    elif num == 2:
        lights = [False, True, True, True, True, True, False]
    elif num == 3:
        lights = [False, True, True, True, False, True, True]
    elif num == 4:
        lights = [True, False, True, True, False, False, True]
    elif num == 5:
        lights = [True, True, False, True, False, True, True]
    elif num == 6:
        lights = [True, True, False, True, True, True, True]
    elif num == 7:
        lights = [False, True, True, False, False, False, True]
    elif num == 8:
        lights = [True, True, True, True, True, True, True]
    elif num == 9:
        lights = [True, True, True, True, False, True, True]
    
    # This segment draws only the lights that are 'on' (True)
    # from the above array.
    if lights[0]:
        canvas.draw_polygon([(x, y + 3), (x + 7, y + 10), (x + 7, y + 24), (x, y + 31)], 2, 'white')
    if lights[1]:
        canvas.draw_polygon([(x + 5, y), (x + 12, y + 7), (x + 26, y + 7), (x + 33, y)], 2, 'white')
    if lights[2]:
        canvas.draw_polygon([(x + 37, y + 3), (x + 30, y + 10), (x + 30, y + 24), (x + 37, y + 31)], 2, 'white')
    if lights[3]:
        canvas.draw_polygon([(x + 5, y + 35), (x + 12, y + 40), (x + 26, y + 40), (x + 33, y + 35), (x + 26, y + 30), (x + 12, y + 30)], 2, 'white')
    if lights[4]:
        canvas.draw_polygon([(x, y + 39), (x + 7, y + 46), (x + 7, y + 60), (x, y + 67)], 2, 'white')
    if lights[5]:
        canvas.draw_polygon([(x + 5, y + 70), (x + 12, y + 63), (x + 26, y + 63), (x + 33, y + 70)], 2, 'white')
    if lights[6]:
        canvas.draw_polygon([(x + 37, y + 39), (x + 30, y + 46), (x + 30, y + 60), (x + 37, y + 67)], 2, 'white') 

# Event Handlers
        
def draw(canvas):
    # Tens digit
    draw_num(canvas, num // 10, 35, 39)
    # Ones digit
    draw_num(canvas, num % 10, 85, 39)
    
def num_in(string):
    global num
    if string.isdigit():
        n = int(string)
        if n < 100:
            num = n
        else:
            print 'Invalid input: Number too large'
    else:
        print 'Invalid input: Not a two digit whole number'
            
def increase_num():
    global num
    num += 1
    num %= 100
    
def decrease_num():
    global num
    num -= 1
    num %= 100

# Frame and Timer

frame = simplegui.create_frame('Digital Numbers', canvas_width, canvas_height) 
frame.add_input('Enter a two digit whole number:', num_in, 70)
frame.add_button('Increase', increase_num, 70)
frame.add_button('Decrease', decrease_num, 70)

# Register Event Handlers

frame.set_draw_handler(draw)

# Start
frame.start()

