# Functions - take an input(s) and return an output
# Scope


# Variables have something called 'scope', which dictates
#   where they can be referred to. There are two types of 
#   scope: global and local. Global variables can be referred
#   to at any point in the program, while local variables can
#   only be referenced within the segment of code (for example,
#   a function) where they appear.

this_one_is_global = "Global"
def do_nothing():
    this_one_is_local = "Local"
    
print "Ex. 1:", this_one_is_global
#print "Ex. 1:", this_one_is_local

this_one_is_global = "Global"
def do_something():
    this_one_is_local = "Local"
    print "Ex. 2:", this_one_is_global
    
do_something()

# Although global variables can be referenced inside methods, if they
#   want to be modified they must be declared as global variables
#   at the beginning of the method.

count = 1

def f():
    new_count = count
    return new_count

print "Ex. 3:", count, f()

def increment():
    global count
    count += 1
    return count

print "Ex. 4:", increment(), increment()

# Errors will occur if the global and assignment statements are reversed

#def increment():
#    count += 1
#    global count
#    return count

# Errors do not occur if count is re-assigned without a global 
#   declaration. This is because CodeSkulptor creates a local variable
#   with the same name as the global variable. Without a global 
#   declaration, this new variable will not have the same value as the
#   global.

count = 1

def increment():
    count = 5
    count += 1
    return count

print "Ex. 5:", increment(), count

# However, just like in regular variable declaration, if variables are
#   not global, they must be assigned a value before use.

def increment():
#    count
#    count = 5
    return count
increment()

def increment():
#    count = count + 1
    return count
increment()

def increment():
#    count += 1
    return count
increment()





