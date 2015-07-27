#--------------------Name Errors -------------------#

################### Example 2 ########################
#NameError: name 'myfunction' is not defined
#Cause: misspelled function name

def my_function(data):
    print "This is some data: " + str(data)
    
myfunction(4)

#fix the spelling of the line above, and the error will disappear.
#When you're naming things in Python, everything counts - 
#capitalization, underscores, digits, etc. It's like a 
#password - everything has to match. Type carefully!