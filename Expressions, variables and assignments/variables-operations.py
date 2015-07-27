# Variables - placeholders for important values
# Operations


# Variables can be operated on, and then stored in another
#   variable or printed to the screen
a = 1
b = 2
c = a + b
print "Ex. 1:", c
print "Ex. 2:", a + b
d = c * 4
print "Ex. 3:", d
print "Ex. 4:", b ** c
print "Ex. 5:", -b
e = a / b + c * d
print "Ex. 6:", e


print "--------"
# Variables can be incremented to keep track of a count

x = 0
# Increments by 1
x = x + 1
print "Ex. 7:", x
# Increments by 2
x = x + 2
print "Ex. 8:", x

x = 2
# Squares x each time
x = x * x
print "Ex. 9:", x
x = x * x
print "Ex. 10:", x
print

# A syntactical shortcut is the '+=' sign, where a += b is 
#   the same as a = a + b
x = 2
x += 3
y = 2
y = y + 3
print "Ex. 11:", x, y
print

# This shortcut can be used with operations other than 
#   addition as well.
x = 5.0
x -= 2
print "Ex. 12:", x
x *= 5
print "Ex. 13:", x
x /= 2
print "Ex. 14:", x
x //= 3
print "Ex. 15:", x
x **= 4
print "Ex. 16:", x


