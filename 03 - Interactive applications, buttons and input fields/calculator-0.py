# starting point for calculator

# intialize globals
store = 12
operand = 3


# define functions that manipulate store and operand
def output():
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    global store, operand
    store, operand = operand, store
    output()


output()
swap()
swap()
