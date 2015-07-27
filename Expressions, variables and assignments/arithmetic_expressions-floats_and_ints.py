# Arithmetic expressions - numbers, operators, expressions
# Floats and Integers


# Integers are whole numbers, while floats can be whole
#   numbers or have fractional parts.

print "Integers:", 5, 19, -2, 37
print "Floats:", -3.4, 5.0, 9.99999, 1.0/3.0
print


# Float to Integer (int): truncates the decimal (leaves it off)
print "Ex. 1:", int(3)
print "Ex. 2:", int(7.4)
print "Ex. 3:", int(1.9)
print "Ex. 4:", int(-1.2)
print "Ex. 5:", int(-2.9)
print

# Integer to float: doesn't change anything
print "Ex. 6:", float(9)
print "Ex. 7:", float(-2)


print "--------"
# Python and CodeSkulptor cannot keep track of an infinite
#   number of decimal places.

print "Ex. 8:", 0.12345678901234567890


print "--------"
# Operations using floats and ints are not exact in python,
#   which leads to some interesting outputs

# These have different final digits and a different number
#   of digits as well
print "Ex. 9: ", 4.0 / 3.0
print "Ex. 10:", 25.0 / 3.0
print
print "Ex. 11:", 1.0 / 6.0
print "Ex. 12:", 13.0 / 6.0
print "Ex. 13:", 601.0 / 6.0
print

# In these ones, the output changes based on the grouping
#   of terms, even though they appear mathematically equivalent
print "Ex. 14:", 5 * 4 / 3
print "Ex. 15:", 5 * (4 / 3)
print "Ex. 16:", 20 / 3
