############
# This is a compilation of the examples from Week 1's Programming Tips.
# Some functions have been renamed like "function1", "function2", etc.
# in order to have multiple versions of the same function within one file.
############


import math


############
# Has a NameError
def volume_cube(side):
    return sidde ** 3

s = 2
print "Volume of cube with side", s, "is", volume_cube(s), "."


############
# Has a NameError
def volume_rect_prism(length, width, height):
    return length * width * height

l = 3
w = 1
h = 4
print "Volume of rectangular prism", l, w, h, "is", volumerectprism(r), "."


############
# Has a NameError
def random_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

print "Sum of two random dice, rolled once:", random_dice()
print "Sum of two random dice, rolled again:", random_dice()


############
# Has an AttributeError
def volume_sphere(radius):
    return 4.0/3.0 * math.Pi * (radius ** 3)

r = 2
print "Volume of sphere of radius", r, "is", volume_sphere(r), "."


############
# Has a TypeError
def area_triangle(base,height):
    return 1.0/2.0 * base * height

b = 5
h = 4
print "Area of triangle with base", b, "and height", h, "is", area_triangle(b), "."


############
# Has a SyntaxError
def identity(x)
    return x

print identity(5)


############
# Has a SyntaxError
def is_mary(x):
    if x = "Mary":
        print "Found Mary!"
    else:
        print "No Mary."

is_mary("Mary")
is_mary("Fred")




############
# Poor readability
def areatri(a, b, c):
    s = (a + b + c) / 2.0
    return math.sqrt(s * (s-a) * (s-b) * (s-c))


############
# Improved readability
def area_triangle_sss(side1, side2, side3):
    """Returns the area of a triangle, given the lengths of its three sides."""
    
    # Use Heron's formula
    s = (side1 + side2 + side3)/2.0
    return math.sqrt(s * (s-side1) * (s-side2) * (s-side3))

base=3
height=4
hyp=5
print "Area of triangle with sides", base, height, hyp, "is", area_triangle_sss(base, height, hyp), "."
