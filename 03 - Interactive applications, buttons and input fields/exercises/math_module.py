# More Operations
# Math Module


# The Math Module contains many useful functions and 
#	constants used in mathematical expressions. To use the 
#	Math Module, it must be imported first.

import math

# Here are some examples of the functions in the Math Module.
#	For explanations of what they do, please check the
#	documentation. Feel free to change these ones around
#	and try more of them from the module.

print "Ex. 1:", math.ceil(.2), math.ceil(-1.4)
print "Ex. 2:", math.floor(4.9999), math.floor(-3.2)
# Note: math.pow() is the same as the '**' symbol
print "Ex. 3:", math.pow(3, 4), 3 ** 4
print "Ex. 4:", math.fabs(-5), math.fabs(5)
print "Ex. 5:", math.sqrt(9), math.sqrt(2)
# Note: all trig function parameters are in radians
print "Ex. 6:", math.sin(0), math.sin(4.5)
print "Ex. 7:", math.radians(180), math.degrees(3.1415926)
print

# The Math Module also contains important constants
# Note: Because they are constants, they do not require ()'s
print "Pi:", math.pi
print "e:", math.e


print "--------"


# Here are some sample functions involving the Math Module

# Pythagorean Theorem (finding the hypotenuse of a right triangle)

def pythagorean(a, b):
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return c

print "Pythagorean Theorem:", pythagorean(3, 4)

# Area of a circle

def area_of_circle(radius):
    area = math.pi * math.pow(radius, 2)
    return area

print "Area of Circle:", area_of_circle(3.4)

# Radioactive decay (approximation)

def radioactive_decay(initial_amount, half_life, time_elapsed):
    x = -0.693 * time_elapsed / half_life
    amount = initial_amount * math.exp(x)
    return amount

print "Radioactive Decay:", radioactive_decay(100, 17.9, 10)






