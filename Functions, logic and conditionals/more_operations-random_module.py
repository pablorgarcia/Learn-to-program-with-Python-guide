# More Operations
# Random


# The Random Module contains many useful functions for 
#   generating random numbers. To use the Random Module,
#   it must be imported first.

import random

# Here are some examples of how to use the functions in the
#   Random Module. Run the program multiple times to see
#   what different random numbers you can get. Check the 
#   documentation for explanations of how the functions work,
#   and for more functions 

# random.choice(list)
# Returns a random value from the list or a random character
#   of a string

print "Choice 1:", random.choice([1,2,7,18,92])
print "Choice 2:", random.choice(["a","b","yes","no"])
print "Choice 3:", random.choice("alphabet")
# Only allows one parameter
#print "Error:", random.choice("hi", "hello")
# Parameter must be a list
#print "Error:", random.choice(4)
print

# random.randint(a, b)
# Returns an int from a to b inclusive

print "Randint 1:", random.randint(1,10)
print "Randint 2:", random.randint(-5, 27)
# Requires two parameters
#print "Error:", random.randint(4)
# Parameters must be integers
#print "Error:", random.randint(0, 4.5)
print

# random.randrange([start], stop[, step])
# Note: parameters in brackets are optional
# Returns an integer from start (inclusive) to stop (not
#   included), skipping numbers by step. If step is not
#   specified (only two parameters), it defaults to 1. If
#   start is also omitted (only one parameter), it defaults
#   to 0.

# Returns odd numbers from [1,9) (1 being the first number 
#   included in the range, and 9 being the first number 
#   excluded in the range)
print "Randrange 1:", random.randrange(1, 9, 2)
# Returns multiples of 5 from 0 to 50
print "Randrange 2:", random.randrange(0, 51, 5)
# Returns ints form [3,10)
print "Randrange 3:", random.randrange(3, 10)
# Returns positive ints less than 200, including 0
print "Randrange 4:", random.randrange(200)
# Returns negative ints greater than -10, including 0
print "Randrange 5:", random.randrange(-10)

# Requires 1, 2, or 3 parameters
#print "Error:", random.randrange()
#print "Error:", random.randrange(1, 2, 3, 4)
# Parameters must be integers
#print "Error:", random.randrange("hi", 4, 5)
#print "Error:", random.randrange(2, 5, .5)
# Stop must be greater than start if both are given
#print "Error:", random.randrange(5, 3, 6)

# Note: if only two arguments are specified, they are 
#   automatically start and stop. It is impossible to specify
#   step without start as well, although start can be set to
#   zero to achieve the same effect. 

# Trying to count by 2 from 0 to 10, including 10
# Doesn't work
#print "Randrange 6:", random.randrange(10, 2) 
# Doesn't work - only goes to 8
print "Randrange 6:", random.randrange(0, 10, 2)
# Does work
print "Randrange 7:", random.randrange(0, 12, 2)
print

# random.random()
# Returns a random number between 0 and 1, including 0

print "Random 1:", random.random()
print "Random 2:", random.random()
print "Random 3:", random.random()
print "--------"
# It is possible to generate random decimal values by
#   performing mathematical operations on random integers

# Random numbers from 0 to 5, excluding 5
x = random.randrange(0, 10)
print "Ex. 1:", x / 2.0

# Random angles in the first quadrant (0 - pi/2)
import math
x = random.randrange(0, 10001)
x = (x / 10000.0) * (math.pi / 2)
print "Ex. 2:", x
print

# Random angles between e and e ** 2
x = random.randrange(0, 10001)
x = (x / 10000.0) * (math.e ** 2 - math.e) + math.e
print "e:", math.e 
print "e ** 2:", math.e ** 2
print "Ex. 3:", x
print

# The general formula - play with the values to test it out

# How many unique random values can be generated
number_of_possibilities = 5 
# First and last values
start = 6
stop = 9
# If you want to include stop and start
x = random.randrange(0, number_of_possibilities + 1)
# If you don't want to include stop
#x = random.randrange(0, number_of_possibilities)
# If you don't want to include start
#x = random.randrange(1, number_of_possibilities + 1)
# If you don't want to include either one
#x = random.randrange(1, number_of_possibilities)
# Calculation
x = (x / float(number_of_possibilities)) * (stop - start) + start
print "Formula A:", x
print

# If you want to include start and not stop, you can also
#   use random.random() to get an unlimited number of
#   possibilities

start = 5
stop = 14
x = random.random()
x = x * (stop - start) + start
print "Formula B:", x
