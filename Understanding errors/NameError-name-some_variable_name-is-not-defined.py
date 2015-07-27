#--------------------Name Errors -------------------#

################### Example 1 ########################
#NameError: name 'message' is not defined
#Cause: the variable "message" was never created before this point

print "I have a message for all my classmates!"
print "My message is that IIPP is an awesome class!"
print message


#The problem is that Codeskulptor doesn't know what "message" is.
#It was never created at all, actually. 
#The code below fixes the problem.

message = "IIPP is an awesome class!"
print message

#If you make a habit of defining your variables early on,
#you will reduce the chances of running into this error. 
