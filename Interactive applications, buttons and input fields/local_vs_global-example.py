# Local vs. Global Variables
# Example

# For this example, there are five versions of the same 
#   program. Three of them work and two of them don't. The
#   goal of the program is to move an object along a number
#   line using a move method, keep track of its location 
#   with the variable loc, and calculate the displacement
#   (always positive) from its starting location with the 
#   displacement method.

# Version one: Doesn't work. The move method throws an error,
#   while the displacement method always prints 0 because
#   the location never changes.

start = 1
loc = start

def move(x):
    loc = loc + x

def displacement():
    return abs(loc - start)

#move(3)
print "Version 1:", displacement()
#move(-2)
print "Version 1:", displacement()
print

# Version two: Works. Fixes version one by declaring variables
#   global at the start of the move method. No global
#   declaration is needed at the start of the displacement
#   method because the values in the global variables loc 
#   and start are not changing.

start = 1
loc = start

def move(x):
    global loc
    loc = loc + x

def displacement():
    return abs(loc - start)

move(3)
print "Version 2:", displacement()
move(-2)
print "Version 2:", displacement()
print

# Version three: Also works. This one returns values instead
#   of attempting to override the global variable. Notice 
#   that the new local variable must have a different name.
#   Notice also that we must assign loc to the value returned
#   by the move method.

start = 1
loc = start

def move(x):
    pos = loc + x
    return pos

def displacement():
    return abs(loc - start)

loc = move(3)
print "Version 3:", displacement()
loc = move(-2)
print "Version 3:", displacement()
print

# Version Four: This one does not work. The loc that is 
#   a parameter in the move method is actually a local 
#   variable instead of a global one, and therefore the 
#   value of the global loc does not change.

start = 1
loc = start

def move(x, loc):
    loc += x
    return loc

def displacement():
    return abs(loc - start)

move(3, loc)
print "Version 4:", displacement()
move(-2, loc)
print "Version 4:", displacement()
print


# Version Five: This one fixes the problem from version 
#   four. This one passes the method the value of loc as a 
#   parameter, and returns the value of the new loc. Note 
#   that in this example the local variable shares the same
#   name as the global one, but is not actually the same 
#   thing.

start = 1
loc = start

def move(x, loc):
    loc += x
    return loc

def displacement():
    return abs(loc - start)

loc = move(3, loc)
print "Version 5:", displacement()
loc = move(-2, loc)
print "Version 5:", displacement()
print




