"""
Compute the length of a rectangle's perimeter,
given its width and height.
"""

# Rectangle perimeter formula
def rectangle_perimeter(width, height):
    return width * 2 + height * 2


# Tests
def test(width, height):
    print "A rectangle " + str(width) + " inches wide and " + str(height),
    print "inches high has a perimeter of",
    print str(rectangle_perimeter(width, height)) + " inches."

# Output
test(4, 7)
test(7, 4)
test(10, 10)