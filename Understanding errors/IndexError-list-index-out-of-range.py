#--------------------Index Errors -------------------#

################### Example 1 ########################
#IndexError: list index out of range
#Cause: trying to access an index that is larger than the list itself
my_list = ["this", "is", "a", "list"]
length_of_list = len(my_list)
big_number = 5   #change this number to be less than or equal to length_of_list to fix the error. 

print "We have " + str(length_of_list) + " elements in this list."

for index in range(big_number):  
    print "The word at index " + str(index) + " is \t" + '"'  + my_list[index] + '"', 
    words_left = length_of_list - index - 1 #minus 1 to account for the fact that we start counting at 0
    print "\t and we have " + str(words_left) + " words left."
    
#By trying to access the 5th element in a 4-element list, we
#trigger an Index Error. Make sure that the last index that you
#try to access is one less than the number of elements in the list. 
#This applies to every data type that contains other
#bits of data - tuples, dictionaries, strings, etc. 


