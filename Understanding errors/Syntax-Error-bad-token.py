#--------------------Syntax Errors -----------------#

################### Example 2 #######################
#SyntaxError: bad token ('"')
#Cause: Forgetting to close your brackets

def say_hello():
    print "Hello world!

    
#Also very common. Make sure that all of your parentheses,
#quotation marks, brackets, etc. come in pairs. Add the 
#missing quotation mark to the end of the second line to 
#get rid of the error. 

#A bit more information: a "token" is a piece of code
#that Python recognizes as meaningful - you can almost think
#of them as coding "atoms". In this case, the token in 
#question is the quotation mark. It means something - 
#namely it indicates the start/end of a string - but Python
#also knows that they always occur in pairs. Since it 
#found only one lonely quotation mark, it generates an 
#error saying so. 