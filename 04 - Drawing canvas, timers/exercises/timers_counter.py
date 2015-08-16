""" The following program should count upward from zero.
Print the counter values 0, 1, 2, … to the console.
Add two lines of Python to make this program work.
Hint: Add a global variable to a timer callback, and start a timer."""

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1

# create timer
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()
