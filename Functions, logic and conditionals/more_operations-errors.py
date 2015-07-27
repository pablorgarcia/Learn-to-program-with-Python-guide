# More Operations
# Errors

# Misspelling the module names can cause an error.

#import randm

# Forgetting to import the correct module before using it
#   causes and error.

#print math.pi
# Importing the wrong one doesn't help
import random          
#print math.pi
import math
print "Ex. 1:", math.pi
print


# Naming a variable or function the same name as a module can
#   also be problematic.

print "Ex. 2:", random.randrange(5)
random = 4
print "Ex. 3:", random
# Random is no longer a module; it is now a variable.
#print "Error:", random.randrange(5)
print

print "Ex. 3:", math.e
def math():
    return 4
print "Ex. 4:", math()
#print "Error:", math.e

# This can technically be fixed by re-importing the modules,
#   but that would be an example of absolutely atrocious
#   programming, so don't do it. It is only done here since
#   this program is supposed to give examples of errors 
#   anyway.
import math
import random


print "--------"
# Misspelling the methods or constant calls of the modules
#   also causes an error. Remember that CodeSkulptor is case
#   sensitive, meaning that the issue could be an incorrectly
#   capitalized letter.

random.randrange(2,4)
#random.randomrange(2,4)
#random.randRange(2, 4)
math.sqrt(4)
#math.squarert(4)
math.pi
#math.pie


# Just like with regular functions, you must use the expected
#   parameters when calling module functions.

#random.randint(9)
#random.randrange("HELLO")

# Note that while the following does not produce a program-
#   crashing error, it does produce a result called 'Not a 
#   Number' which is not very helpful and cannot be used 
#   the same way other numbers can.
print math.sqrt("4")
print math.sqrt("4") + 2
print math.sqrt("i")

