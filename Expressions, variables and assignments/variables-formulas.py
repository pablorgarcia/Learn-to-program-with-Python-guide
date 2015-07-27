# Variables - placeholders for important values
# Formulas


# Variables can be parts of re-useable formulas. When you
#   change the value of one variable, the computer will
#   automatically recalculate the other value for you.
#   Try changing the value of the first variable in each
#   simple formula and see what happens to the output.

# Area of a square
side = 3
area = side ** 2
print "Ex. 1:", area

# Hours to minutes
hours = 3
minutes = hours * 60
print "Ex. 2:", minutes

# Hours to seconds
hours = 2.5
minutes = hours * 60
seconds = minutes * 60
print "Ex. 3:", seconds
# or
seconds = hours * 60 * 60
print "Ex. 4:", seconds
# or
seconds = hours * 3600
print "Ex. 5:", seconds

# Discriminant of the quadratic formula
a = 6
b = -2
c = -1
discriminant = b ** 2 - (4 * a * c)
print "Ex. 6:", discriminant

# Volume of a square pyramid
length = 2
width = 4
height = 5
volume = length * width * height * 1 / 3.0
print "Ex. 7:", volume

# Float to int
f = 9.5
i = int(f)
print "Ex. 8:", i


