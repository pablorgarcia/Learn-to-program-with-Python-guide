# Compute the circumference of a circle, given the length of its radius.

# Circle circumference formula
import math
def circle_circumference(radius):
    return 2 * math.pi * radius

# Tests
def test(radius):
    print "A circle with a radius of " + str(radius),
    print "inches has a circumference of",
    print str(circle_circumference(radius)) + " inches."

# Output
test(8)
test(3)
test(12.9)