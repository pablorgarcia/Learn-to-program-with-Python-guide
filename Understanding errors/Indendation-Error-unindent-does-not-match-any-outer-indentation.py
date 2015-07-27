#--------------------Syntax Errors -------------------#

################### Example 5 ########################
#IndentationError: unindent does not match any outer indentation.
#Cause: under-indenting a line of code. 

def my_badly_indented_function():
    print "This line is indented correctly - four spaces ",
    "from the edge."
   print "This line is not - it is only three spaces from ", 
    "the edge."
    
#Because Python pays attention to spaces, an indentation
#error actually counts as a syntax error. Officially,
#an IndentationError is a *subclass* of the SyntaxErrors.
#Note that under-indenting something produces this result,
#while over-indenting something produces a SyntaxError: bad
#input.
    
    
