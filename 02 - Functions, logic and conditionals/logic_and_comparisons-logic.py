# Logic and Comparisons
# Logic


# There are some rules or operations that can be done on 
#   boolean expressions to simplify them. Remember to change
#   the values of the variables to test different combinations.

a = True
b = False
c = True

# Associative Property - (a and b) and c = a and (b and c)
#                        (a or b) or c = a or (b or c)

print "Ex. 1:", (a and b) and c, a and (b and c)
print "Ex. 2:", (a or b) or c, a or (b or c)


# Commutative Property - a and b = b and a
#                        a or b = b or a

print "Ex. 3:", a and b, b and a
print "Ex. 4:", a or b, b or a


# Distributive Property - a and (b or c) = (a and b) or (a and c)

print "Ex. 5:", a and (b or c), (a and b) or (a and c)
print


# Identity - True and a = a, False and a = False
#            True or a = True, False or a = a        

print "Ex. 6:", True and a, a
print "Ex. 7:", False and a, False
print "Ex. 8:", True or a, True
print "Ex. 9:", False or a, a


# Redundancy - a and a = a, a and not a = False
#              a or a = a, a or not a = True

print "Ex. 10:", a and a, a
print "Ex. 11:", a and not a, False
print "Ex. 12:", a or a, a
print "Ex. 13:", a or not a, True
print


# DeMorgan's Law - not (a and b) = not a or not b
#                  not (a or b) = not a and not b

print "Ex. 14:", not (a and b), not a or not b
print "Ex. 15:", not (a or b), not a and not b


print "--------"
# Example problems

print "Ex. 16:", a or (a and b)
print "       ", (a and True) or (a and b)
print "       ", a and (True or b)
print "       ", a and True
print "       ", a
print

print "Ex. 17:", a and not (a or b)
print "       ", a and (not a and not b)
print "       ", (a and not a) and not b
print "       ", False and not b
print "       ", False
print




