# String Processing
# Input Checking

# Checking for valid input can avoid errors in your program.
# Here are some examples of functions re-worked so that
# invalid inputs no longer crash the program.

import simplegui

# Global Variables
canvas_width = 300
canvas_height = 300

# Event Handlers

# Number of diagonals in a polygon
# For this method, num_sides must be an integer greater than 2.
def num_diagonals(num_sides):
    if num_sides.isdigit():
        num_sides = int(num_sides)
        if num_sides > 2:
            ans = num_sides * (num_sides - 3) / 2
            print 'Number of Diagonals: ' + str(ans)
        else:
            print 'Error: Invalid input. Please enter an integer greater than 2.'
    else:
        print 'Error: Invalid input. Please enter an integer greater than 2.'
    print

# Checks to see if a given string is a valid multiple-choice
# answer. (Valid answers are the letters a, b, c, and d)
def is_valid_answer(ans):
    if len(ans) == 1:
        if ans == 'a' or ans == 'b' or ans == 'c' or ans == 'd':
            print ans, 'is valid.'
        else:
            print ans, 'is not valid.'
    else:
        print ans, 'is not valid.'

# Checks to see if a given string is a valid move in rock-paper-scissors.
# Allows any combination of upper and lowercase letters to be used.
def is_valid_move(move):
    # Using a second variable prevents the original value
    # from being changed so it can be printed later.
    m = move.lower()
    if m == 'rock' or m == 'paper' or m == 'scissors':
        print move, 'is valid.'
    else:
        print move, 'is not valid.'

# Frame
frame = simplegui.create_frame('Functions', canvas_width, canvas_height, 150) 

# Register Event Handlers
frame.add_input('Number of sides:', num_diagonals, 100)
frame.add_input('Multiple choice answer:', is_valid_answer, 100)
frame.add_input('Valid RPS move:', is_valid_move, 100)

# Start Frame
frame.start()