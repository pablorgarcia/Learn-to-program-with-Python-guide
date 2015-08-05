# Arithmetic expressions - numbers, operators, expressions
# Order of Operations


# Have you seen this problem on the internet?

# The first example is not 0, because multiplication comes
#   before addition in the order of operations
print "Ex. 1:", 1 + 1 + 1 + 1 + 1 * 0

# In this one, the addition is performed first due to the 
#   parenthesis, so the answer is 0
print "Ex. 2:", (1 + 1 + 1 + 1 + 1) * 0

# Another example of the power of parenthesis
print "Ex. 3:", 1 + 1 + 1 + (1 + 1) * 0


print "--------"
# Parenthesis can change the value of an expression by 
#   changing the order in which operations are computed

#The following examples have the same numbers with the same
#   operators in the same order, but different results
print "Ex. 4:", 5 + 6 / 2 - 3
print "Ex. 5:", (5 + 6) / 2 - 3
print "Ex. 6:", 5 + 6 / (2 - 3)
print "Ex. 7:", (5 + 6) / (2 - 3)


print "--------"
# Here are a few more examples of Order of Operations
# Remember: Please Excuse My Dear Aunt Sally
#           (), **, * and / and //, + and -
# Try to guess what they will print out before looking
#   at the output
print "Ex. 8:", 4 / 2 * 5
print "Ex. 9:", 4 / (2 * 5)
print
print "Ex. 10:", 4 - 5 * 3
print "Ex. 11:", (4 - 5) * 3
print
print "Ex. 12:", 3 * 4 ** 2
print "Ex. 13:", 3 ** 4 * 2
print "Ex. 14:", 3 ** (4 * 2)
print
print "Ex. 15:", 5 + 6 * 3
print "Ex. 16:", 6 * 3 + 5
print
print "Ex. 17:", 7 + 3 // 2
print "Ex. 18:", (7 + 3) // 2


