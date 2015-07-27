#--------------------Syntax Errors -----------------#

################### Example 3b  #######################
#SyntaxError: 'return' outside function
#Cause: bad indentation
def do_some_math(a, b):
    value = a + b
return value

#Add a tab in front of "return" to fix this one. 

#Bad indentation causes a ton of problems in Python.
#There are many more SyntaxErrors that look similar to
#3a and 3b. If you get a syntax error, this is one of the 
#first things you should check!
