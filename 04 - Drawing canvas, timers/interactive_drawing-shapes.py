# Interactive Drawing
# Shapes

# This is an overview of the shapes that can be drawn on the
# canvas. For full details, please look at the documentation.
# If you are having issues figuring out which shape is drawn
# by which line of code, try commenting some of them out.
# General notes: It is acceptable to use either () or [] when
# listing points. However, be careful that you match
# the number and type of () or [] that you are using. Also,
# polygons and circles have optional parameters that allow 
# you to select a fill color.

import simplegui
import math

# Global Variables
canvas_width = 600
canvas_height = 600

# Event Handlers
def draw(canvas):
    # Line Segment
    point_one = (10, 20)
    point_two = (300, 20)
    line_width = 5
    line_color = 'Red'
    canvas.draw_line(point_one, point_two, line_width, line_color)
    canvas.draw_line((335, 25), (550, 50), 25, 'Blue')

    # Connected Line Segments

    # Note that any number of points are allowed, and they 
    # connect in the order that they are listed in the 
    # method parameters. (same goes for polygons)
    point_one = (30, 50)
    point_two = (130, 150)
    point_three = (170, 100)
    line_width = 10
    line_color = 'Purple'
    canvas.draw_polyline([point_one, point_two, point_three], line_width, line_color)
    canvas.draw_polyline([(500, 150), (400, 100), (342, 117), (301, 151), (200, 150)], 3, 'Orange')

    # Polygons - All

    point_one = (50, 200)
    point_two = (80, 260)
    point_three = (170, 210)
    point_four = (100, 225)
    point_five = (75, 205)
    line_width = 5
    line_color = 'Aqua'
    fill_color = 'Lime'
    canvas.draw_polygon([point_one, point_two, point_three, point_four, point_five], line_width, line_color)
    point_one = (250, 200)
    point_two = (280, 260)
    point_three = (370, 210)
    point_four = (300, 225)
    point_five = (275, 205)
    canvas.draw_polygon([point_one, point_two, point_three, point_four, point_five], line_width, line_color, fill_color)
    canvas.draw_polygon([(450, 200), (550, 200), (450, 300), (550, 300)], 10, 'Navy', 'Olive')

    # Polygons - Rectangles

    # Same syntax as polygons, just using four points
    canvas.draw_polygon([(50, 300), (50, 350), (150, 350), (150, 300)], 8, 'Green')
    # Simple formulas:
    # Top left corner = (a, b), Bottom right = (c, d)
    a = 200
    b = 300
    c = 220
    d = 350
    canvas.draw_polygon([(a, b), (a, d), (c, d), (c, b)], 2, 'Yellow', 'Yellow')
    # Top left corner = (a, b)
    a = 275
    b = 300
    width = 140 # For squares, width = height
    height = 75
    canvas.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)], 20, 'Fuchsia')

    # Polygons - Triangles

    # Same syntax as polygons, just using three points
    canvas.draw_polygon([(50, 420), (150, 470), (200, 370)], 5, 'Teal', 'Teal')
    # For right triangles:
    a = 200
    b = 450
    width = 100 # For one type of isosceles triangle, width = height
    height = 100
    canvas.draw_polygon([(a, b), (a + width, b), (a, b + height)], 6, 'White')
    # Formula for equilateral triangles:
    a = 450
    b = 450
    width = 100
    canvas.draw_polygon([(a, b), (a + width, b), ((2 * a + width) / 2, b + width / 2 / math.tan(math.pi / 6))], 5, 'Black', 'Gray')

    # Circles
    center = (75, 550)
    radius = 30
    line_width = 5
    line_color = 'Silver'
    fill_color = 'Maroon'
    canvas.draw_circle(center, radius, line_width, line_color)
    center = (150, 550)
    canvas.draw_circle(center, radius, line_width, line_color, fill_color)
    canvas.draw_circle((350, 550), 50, 10, 'Red')
    canvas.draw_circle((350, 550), 25, 10, 'Blue', 'Blue')

# Frame
frame = simplegui.create_frame('Shapes', canvas_width, canvas_height) 

# Register Event Handlers
frame.set_draw_handler(draw)

# Remember to start the frame
frame.start()