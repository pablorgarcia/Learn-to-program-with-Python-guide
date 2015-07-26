print 'The modulus function is a form of division where the remainder is returned. It is represented by the % symbol.'
print
print "7 / 2 =", 7 / 2
print "7 % 2 =", 7 % 2
print
print "11 / 4 =", 11 / 4
print "11 % 4 =", 11 % 4
print
print "2 / 7 =", 2 / 7
print "2 % 7 =", 2 % 7
print
print "4 / 4 =", 4 / 4
print "4 % 4 =", 4 % 4
print

print 'Modulus can also be done on fractions and decimals.'
print
print "5.2 / 3:", 5.2 / 3
print "5.2 % 3:", 5.2 % 3
print
print "2 % 1.5:", 2 % 1.5
print
print "3.5 % .5:", 3.5 % .5
print
print "(5.0 / 4.0) % 3.0:", (5.0 / 4.0) % 3.0
print
print "2.75 % (1.0 / 2.0):", 2.75 % (1.0 / 2.0)
print

print 'Modulus is done at the same time as division and multiplication in the order of operations'
print
print "5 + 3 % 2 =", 5 + 3 % 2
print "(5 + 3) % 2 =", (5 + 3) % 2
print
print "6.0 / 3.0 % 5.0 =", 6.0 / 3.0 % 5.0
print "6.0 % 5.0 / 3.0 =", 6.0 % 5.0 / 3.0
print

print 'Remember that division in Python and CodeSkulptor is not exact.'
print
print "5.4 % 3 =", 5.4 % 3
# Almost zero...the e-17 means: * (10 ** -17), which is
#	a really small number
print ".9 % .3 =", .9 % .3


print "--------"
print 'Modulus can also be used with negative numbers.'
print 'The first number dictates which direction you would move'
print 'along a number line to get the answer, and the second'
print 'number dictates which way the line is facing.'

print 3 % 8, -3 % -8, -3 % 8, 3 % -8
print

print 'Number line is positive, direction is positive'

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


