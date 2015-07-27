#--------------------Token Errors -------------------#

################### Example 1 ########################
#TokenError: EOF in multi-line statement
#Cause: forgetting to close a bracket
good_list = [1, 1, 2, 3, 5, 8]
bad_list = [4, 8, 15, 16, 23, 42

            
#This Token Error usually pops up when you forget to close
#a bracket. It could be for a [list], a {dictionary}, 
#a (tuple) or a [(set)]. 

#For the curious, "EOF" is a token that means End Of File.
#It's invisible to you, but not to Python. The EOF token
#is not allowed to appear inside a list. So in bad_list,
#we open the list with [, put in a couple values, 
#and then when there are no more values in the line, we 
#come to the EOF token...without ever having come across the 
#closing bracket! So since Python still thinks we're inside
#the list, and because EOF isn't allowed inside a list, 
#we get the Token Error. 