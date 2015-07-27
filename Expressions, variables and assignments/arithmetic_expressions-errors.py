# Arithmetic expressions - numbers, operators, expressions
# Errors


# Here are some errors you may come across, and some of the
#   ways they can be caused, as well as some notes on code
#   readability

# Multiple Operands
# '+' and '-' signs can appear alone in front of a number, 
#   but '*' and '/' signs cannot. However, the '+' sign is
#   utterly useless and should not be used.
print "Ex. 1:", +1
print "Ex. 2:", +(-1)
print "Ex. 3:", +-1
print "Ex. 4:", -2
print "Ex. 5:", -(+2)
print "Ex. 6:", +-2
print

# Proper spacing is important to avoid confusion

# Looks invalid at first, but is actually 3 - (-1)
print "Ex. 7:", 3--1
print "Ex. 8:", 3 - -1
print

# Uncomment the lines one at a time to see the error messages
#print *8
#print /8
#print + *8
#print - /8

# Remember the meanings of '//' and '**'

# Looks like an error, but is actually an exponent
print "Ex. 9:", 2 ** 4

# Looks like an error, but is actually integer division
print "Ex. 10:", 4.0 // 3.0


print "--------"
# Operations must be followed by a number

# Uncomment the lines to see the errors
#print *
#print 5 /
#print 6 -
#print 78 + 3 +
#print 5 / * 9
#print 8 + * 7

# Numbers/expressions must be separated by an operand

# Uncomment the lines to see the errors
#print 5 6
#print 5t
# Note the difference:
#print 4(5)
print "Ex. 11:", 4 * (5)


print "--------"
# Be especially careful in cases of missing parenthesis

# Missing opening parenthesis
#print 7 * 4)
#print (8 - 2) * 6)

# Missing closing parenthesis
# This one is tricky, because the error does not appear on
#   the line with the missing parenthesis
#print (
#print ((9 + 3)

print "Ex. 12:", 4
# Now comment out the above line, and see how the missing
#   parenthesis error messages change
