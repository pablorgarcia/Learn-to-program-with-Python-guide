# Logic and Comparisons
# Booleans


# Booleans are a value that can either be 'True' or 'False'.
#   Note that the color of the words is different.

print True
print False
print

# Booleans can also be stored in variables

a = True
b = False
print "a:", a
print "b:", b


print "--------"
# The operators 'and', 'or', and 'not' can be used to evaluate
#   a boolean expression.

# 'and' is true only if both operands are true
print "True and True:", True and True
print "True and False:", True and False
print "False and True:", False and True
print "False and False:", False and False
print

# 'or' is true if either operand is true
print "True or True:", True or True
print "True or False:", True or False
print "False or True:", False or True
print "False or False:", False or False
print

# 'not' only requires one operand, and it returns True if it
#   is False, and False if it is True
print "not True:", not True
print "not False:", not False
print

# Variables can also store the results of these operations
a = True or False
b = True and False
print "a:", a
print "b:", b


print "--------"
# Boolean operands have an order of operations, just like
#   regular operands do. The order is: not, and, or


a = False
b = True
c = False
d = True

print "Ex. 1:", not a or b
print "Ex. 2:", (not a) or b
print "Ex. 3:", not (a or b)
print
print "Ex. 4:", b or a and c
print "Ex. 5:", b or (a and c)
print "Ex. 6:", (b or a) and c
print
print "Ex. 7:", b and d and c
print "Ex. 8:", b and d and not c
print "Ex. 9:", a or b or c
print "Ex. 10:", a or not b or c
print
print "Ex. 11:", a and not b or c
print "Ex. 12:", c or not b and a

