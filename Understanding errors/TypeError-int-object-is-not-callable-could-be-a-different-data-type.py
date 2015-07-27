#--------------------Type Errors -------------------#

################### Example 4 ########################
#TypeError: 'int' object is not callable
#Cause: Missing operators between operands

print 5(3)


#Many of us are taught in school that you can write
#multiplication like the statement above, with no operator.
#Python doesn't accept this - you must use the '*' symbol
#to indicate multiplication. 

#More generally, the "object not callable" error probably 
#means that you're trying to treat something like an object
#when it really isn't. Check your variable types using 
#Python's type() command, like this:

print type(5)