"""
Write a function circle_circumference that takes a single parameter radius
corresponding to the radius of a circle in inches
and returns the the circumference of a circle with radius radius in inches.
Do not use π=3.14, instead use the math module to supply
a higher-precision approximation to π.
"""

# Circle area formula
import math
def circle_area(radius):
    return math.pi * radius ** 2 

# Tests
def test(radius):
    print "A circle with a radius of " + str(radius),
    print "inches has an area of",
    print str(circle_area(radius)) + " square inches."

# Output
test(8)
test(3)
test(12.9)


# A circle with a radius of 8 inches has an area of 201.06192983 square inches
# A circle with a radius of 3 inches has an area of 28.2743338823 square inches
# A circle with a radius of 12.9 inches has an area of 522.792433484 square inches