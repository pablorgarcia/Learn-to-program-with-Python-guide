"""
Write a function interval_intersect that takes parameters a, b, c,
and d and returns True if the intervals [a,b] and [c,d] intersect and False otherwise.
While this test may seem tricky, the solution is actually very simple
and consists of one line of Python code. (You may assume that a<b and c<d.)
"""

# Interval intersection formula
def interval_intersect(a, b, c, d):
    """Returns whether the intervals [a,b] and [c,d] intersect."""
    return (c <= b) and (a <= d)


# Tests
def test(a, b, c, d):
    """Tests the interval_intersect function."""
    print "Intervals [" + str(a) + ", " + str(b) + "] and [" + str(c) + ", " + str(d) + "]",
    if interval_intersect(a, b, c, d):
        print "intersect."
    else:
        print "do not intersect."


# Output
test(0, 1, 1, 2)
test(1, 2, 0, 1)
test(0, 1, 2, 3)
test(2, 3, 0, 1)
test(0, 3, 1, 2)

#Intervals [0, 1] and [1, 2] intersect.
#Intervals [1, 2] and [0, 1] intersect.
#Intervals [0, 1] and [2, 3] do not intersect.
#Intervals [2, 3] and [0, 1] do not intersect.
#Intervals [0, 3] and [1, 2] intersect.