# Write a function powerball that takes no arguments and prints the message
# "Today's numbers are %, %, %, %, and %. The Powerball number is %.".
# The first five numbers should be random integers in the range [1,60),
# at least 1, but less than 60.
# In reality, these five numbers must all be distinct,
# but for this problem, we will allow duplicates.
# The Powerball number is a random integer in the range [1,36),
# at least 1 but less than 36.
# Use the random module and the function random.randrange to generate the appropriate random numbers.

# Powerball function
import random

def powerball():
    print "Today's numbers are " + str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ", and",
    print str(random.randrange(1, 60)) + ". The Powerball number is",
    print str(random.randrange(1, 36)) + "."

# Output
powerball()
powerball()
powerball()

# Today's numbers are X, N, Y, J, and W. The Powerball number is T.
# Today's numbers are X, N, Y, J, and W. The Powerball number is T.
# Today's numbers are X, N, Y, J, and W. The Powerball number is T.