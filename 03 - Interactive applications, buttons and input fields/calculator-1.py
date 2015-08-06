# more of the calculator application

import simplegui


# intialize globals
store = 12
operand = 3


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()

# create frame
f = simplegui.create_frame("Calculator",300,300)

# register event handlers
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)


# get frame rolling
f.start()
