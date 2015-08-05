# Logic and Comparisons
# Expressions


# The comparison operations can be used at the same time as
#   the logic operations. The comparison operations are after
#   'not,' but before 'and' in the order of operations. 

a = True
b = False
x = 4
y = 6

print "Ex. 1:", a or b == False
print "Ex. 2:", (a or b) == False
print "Ex. 3:", x < y or x > 2
print "Ex. 4:", x == y and x > 0
print "Ex. 5:", x != y and x > 7
print "Ex. 6:", not b and x > 1


print "--------"
# For fun: you can combine boolean operations with '==' and
#   '<' to make all of the other comparison operations. Feel
#   free to change the numbers to test them out. See if you
#   can come up with alternate ways!

a = 4
b = 5

# !=

print "Ex. 7:", not (a == b)
print "Ex. 8:", a != b 
print

# >
print "Ex. 9:", not (a < b) and not (a == b)
print "Ex. 10:", a > b
print

# <=
print "Ex. 11:", (a < b) or (a == b)
print "Ex. 12:", a <= b
print

# >=
print "Ex. 13:", not (a < b)
print "Ex. 14:", a >= b
print


