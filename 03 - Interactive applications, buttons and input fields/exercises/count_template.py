# Functions to manipulate global variable count

count = 0

# Reset global count to zero.
def reset():
    global count
    count = 0
# Increment global count.
def increment():
    global count
    count += 1
# Decrement global count.
def decrement():
    global count
    count -= 1
# Print global count.
def print_count():
    print count
    
# Test
# note that the GLOBAL count is defined inside a function
reset()     
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

# Output
#1
#2
#-2