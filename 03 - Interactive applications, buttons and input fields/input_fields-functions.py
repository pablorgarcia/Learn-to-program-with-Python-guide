# Input Fields
# Functions


# Input fields can be used to call functions multiple times
#   while the program is running. Here are functions from
#   week one that can now be called using input fields.
#   There is a difference: input fields always return strings,
#   but the methods require numbers. This is solved using the
#   int() and float() methods.
# Remember to hit 'enter' after typing data into the input
#   fields to give it to the computor. Be careful! If you
#   enter the wrong type of data, an error can occur.

import simplegui

# Global Variables

canvas_width = 300
canvas_height = 300

# Event Handlers

# Number of diagonals in a polygon
def num_diagonals(num_sides):
    num_sides = int(num_sides)
    ans = num_sides * (num_sides - 3) / 2
    print "Number of Diagonals:"
    print ans
    print

# Fat cat is Fat :)
def fat_cat(adjective):
    print "Fat cat:"
    print adjective, "cat is", adjective
    print
    
# Prints the type of triangle given the largest angle 
#   measurement in degrees
def print_triangle_type(degrees):
    degrees = float(degrees)
    print "Triangle Type:"
    if degrees > 90 and degrees < 180:
        print "Triangle is obtuse!"
    elif degrees == 90:
        print "Triangle is right!"
    elif degrees < 90 and degrees > 0:
        print "Triangle is acute!"
    else:
        print "Triangle does not exist!"
    print
        

    
# Frame

frame = simplegui.create_frame("Functions", canvas_width, canvas_height, 150) 

# Register Event Handlers

frame.add_input("Number of sides:", num_diagonals, 100)
frame.add_input("Adjective:", fat_cat, 100)
frame.add_input("Angle measure: (degrees)", print_triangle_type, 100)

# Start Frame

frame.start()