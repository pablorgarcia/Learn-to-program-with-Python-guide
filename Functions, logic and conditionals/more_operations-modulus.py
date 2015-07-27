# More Operations - placeholders for important values
# Modulus


# The modulus function is a form of division where the 
#   remainder is returned. It is represented by the '%' symbol.

print "Ex. 1:", 11 % 4
print "Ex. 2:", 2 % 7
print "Ex. 3:", 4 % 4
print

# Modulus can also be done on fractions and decimals.

print "Ex. 4:", 5.2 % 3
print "Ex. 5:", 2 % 1.5
print "Ex. 6:", 3.5 % .5
print "Ex. 7:", (5.0 / 4.0) % 3.0
print "Ex. 8:", 2.75 % (1.0 / 2.0)
print

# Modulus is done at the same time as division and multiplication
#   in the order of operations

print "Ex. 9:", 5 + 3 % 2
print "Ex. 10:", (5 + 3) % 2
print
print "Ex. 11:", 6.0 / 3.0 % 5.0
print "Ex. 12:", 6.0 % 5.0 / 3.0
print

# Remember that division in Python and CodeSkulptor is not
#   exact.

print "Ex. 13:", 5.4 % 3
# Almost zero...the e-17 means: * (10 ** -17), which is
#   a really small number
print "Ex. 14:", .9 % .3


print "--------"
# Modulus can also be used with negative numbers. The
#   first number dictates which direction you would move
#   along a number line to get the answer, and the second
#   number dictates which way the line is facing. 

print 3 % 8, -3 % -8, -3 % 8, 3 % -8
print

# Number line is positive, direction is positive

print 5 % 3, 2 % 5

# Number line is positive, direction is negative
# Same as (b - (a % b))

print -5 % 3, -2 % 5

# Number line is negative, direction is negative
# Same as ( -(a % b))

print -5 % -3, -2 % -5

# Number line is negative, direction is positive
# Same as ( -(b - (a % b)))

print 5 % -3, 2 % -5

