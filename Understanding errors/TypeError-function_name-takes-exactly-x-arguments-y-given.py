#--------------------Type Errors -------------------#

################### Example 2 ########################
#TypeError: give_me_two_numbers() takes exactly 2 arguments (1 given)
#Cause: the function definition requires X number of arguments, but Y were supplied

def give_me_two_numbers(num1, num2):
    print "You gave me " + str(num1) + " and " + str(num2)
    
give_me_two_numbers(4)

#When give_me_two_numbers was defined, it declared that
#it needed two arguments, num1 and num2. When we went to 
#use it though, we only gave it one of those, so we get 
#a TypeError back - we tried to use the function in a 
#way that it wasn't meant to be used. 
