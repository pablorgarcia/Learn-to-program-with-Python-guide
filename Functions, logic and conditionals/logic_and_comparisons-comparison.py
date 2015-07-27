# Logic and Comparisons
# Comparison


# Values can be compared using ==, !=, <, >, <=, and >=

# == checks to see if two values are equal.

print "Ex. 1:", 2 == 2
print "Ex. 2:", 4.5 == 4
print "Ex. 3:", 9.23 == 9.23
print "Ex. 4:", "hi" == "hi"
print "Ex. 5:", "hi" == "hello"
# Note: Capitalization matters
print "Ex. 6:", "hi" == "Hi"
print "Ex. 7:", "40" == 40
print "Ex. 8:", int("40") == 40
print "Ex. 9:", "40" == str(40)
print "Ex. 10:", True == True
print "Ex. 11:", True == False
print

# != checks to see if two values are not equal

print "Ex. 12:", 2 != 2
print "Ex. 13:", 4.5 != 4
print "Ex. 14:", 9.23 != 9.23
print "Ex. 15:", "hi" != "hi"
print "Ex. 16:", "hi" != "hello"
# Note: Capitalization matters
print "Ex. 17:", "hi" != "Hi"
print "Ex. 18:", "40" != 40
print "Ex. 19:", int("40") != 40
print "Ex. 20:", "40" != str(40)
print "Ex. 21:", True != True
print "Ex. 22:", True != False
print

# < checks to see if the value on the left is less than the 
#   value on the right

print "Ex. 23:", 4 < 5
print "Ex. 24:", 6.5 < 2
print "Ex. 25:", 4 < 4
print "Ex. 26:", -4 < -2
print

# > checks to see if the value on the left is greatr than 
#   the value on the right

print "Ex. 27:", 4 > 5
print "Ex. 28:", 6.5 > 2
print "Ex. 29:", 4 > 4
print "Ex. 30:", -4 > -2
print

# <= checks to see if the value on the left is less than or
#   equal to the value on the right

print "Ex. 31:", 5 <= 6
print "Ex. 32:", 4.5 <= 4.5
print "Ex. 33:", -3 <= -9
print

# >= checks to see if the value on the left is greater than
#   or equal to the value on the right

print "Ex. 31:", 5 >= 6
print "Ex. 32:", 4.5 >= 4.5
print "Ex. 33:", -3 >= -9


print "--------"
# Variables can also be assigned to the results of these 
#   expressions.

a = 7 == 4
b = 3 <= 5
print "a:", a
print "b:", b
print


# Typing these operations incorrectly can cause errors. Be
#   especially careful to use double equals signs when
#   comparing two values, and only one equals sign when 
#   assigning a new value to a variable
#print 1 = 3
#print 1 => 4
#a = 3 = 2

# Be careful when comparing and assigning to variables. 
c = 3
d = 4
# This statement assigns e to either True or False,
#   depending on the values of c and d
e = c == d
# This statement assigns c to the value of d, then assigns
#   this value to f as well.
f = c = d
print "e:", e
print "f:", f
print "c:", c
print "d:", d


print "--------"
# These comparison operations are part of the order of
#   operations as well. < and > come after addition and 
#   subtraction, followed by the ==, !=, <=, and >=
#   operations. Last in the order of operations is the 
#   single '=', which stands for assignment.

print "Ex. 1:", 3 - 4 < 5 - 6
print "Ex. 2:", 17 * 4 == 34 * 2
print "Ex. 3:", 3 < 4 == 5 > 6
print "Ex. 4:", 4 <= 4 == 5 >= 3
print "Ex. 5:", (4 <= 4) == (5 >= 3)

# It is especially easy to forget to use two equals signs
#   when testing mathematical expressions
#print "Error:", 3 * 4 = 4 * 3


