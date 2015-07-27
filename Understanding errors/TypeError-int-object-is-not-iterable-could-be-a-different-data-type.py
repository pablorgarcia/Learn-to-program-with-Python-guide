#--------------------Type Errors -------------------#

################### Example 3 ########################
#TypeError: 'int' object is not iterable
#Cause: Trying to loop over something that doesn't allow it

bucket = 5
#bucket = ['1', '2', '3', '4', '5']
for value in bucket:
    print "Hello there!"
    
    
#An integer is a primitive type - it doesn't contain anything
#other than its own value. In contrast, something like a list
#can contain other things. This makes it "iterable" . This 
#TypeError generally indicates that something in your 
#for loop header is a primitive type, so you won't be able
#to loop through it. To fix the error above, use the 
#second declaration of "bucket". 