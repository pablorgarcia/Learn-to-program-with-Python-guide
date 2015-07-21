# Compute the area of a triangle (using Heron's formula), given its side lengths.

# Triangle area (Heron's) formula
# Hint:  Also define point_distance as use it as a helper function.
def point_distance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
    
def triangle_area(x0, y0, x1, y1, x2, y2):
    # Compute the lengths of the three sides.
    a = point_distance(x0, y0, x1, y1)
    b = point_distance(x0, y0, x2, y2)
    c = point_distance(x1, y1, x2, y2)
    
    # Compute the semi-perimeter length, i.e., half of the perimeter length.
    s = (a + b + c) / 2
    
    # Compute the area according to Heron's formula.
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


# Tests
def test(x0, y0, x1, y1, x2, y2):
    
    print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
    print "(" + str(x1) + "," + str(y1) + "), and",
    print "(" + str(x2) + "," + str(y2) + ") has an area of",
    print str(triangle_area(x0, y0, x1, y1, x2, y2)) + "."

# Output
test(0, 0, 3, 4, 1, 1)
test(-2, 4, 1, 6, 2, 1)
test(10, 0, 0, 0, 0, 10)


#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.