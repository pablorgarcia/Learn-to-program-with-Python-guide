# Logic and Comparisons
# if-elif-else


# You can control which statements of your program execute
#   using if, elif, and else statements. They consist of the
#   keywords if, elif (else-if), or else, a boolean or boolean 
#   expression (for if and elif), a colon, and then some 
#   code in the body

# Change the values of the following variables to see how they
#   affect which statements are printed.

conditional_statement = True or False 
boolean = True

if conditional_statement:
    print "The code following the 'if' was true, so this statement was printed."
    print
elif boolean:
    print "The code following the 'if' wasn't true, but the code following the 'elif' was,"
    print "so these statements were printed."
    print
else:
    print "The code following the 'if' and the code following the 'elif' were both false,"
    print "so these statements were printed instead."
    print
    
# An 'if' statement can be followed by any number of 'elif'
#   statements, followed by 0 or 1 'else' statement. 'if' 
#   statements can also be followed by other 'if' statements

a = True
b = False
c = True

if a:
    print "Ex. 1 - a"

if a:
    print "Ex. 2 - a"
elif b:
    print "Ex. 2 - b"
elif c:
    print "Ex. 2 - c"
    
if a:
    print "Ex. 3 - a"
else:
    print "Ex. 3 - not a"

if a:
    print "Ex. 4 - a is True!"
if b:
    print "Ex. 4 - b is True!"
if c:
    print "Ex. 4 - c is True!"
    
    
# Errors can be caused by incorrect order of if-elif-else
#   blocks, incorrect indentation, by leaving out the ':'
#   at the end of the line, and by not putting a boolean 
#   or boolean expression after the if.
    
a = True
b = False
    
# Incorrect order / missing if statements

#if a:
#    pass
#else:
#    pass
#elif b:
#    pass
    
#else:
#    pass

#elif:
#    pass
    
# Incorrect indentation

if a:
    x = 4
#   x = 3
#     x = 2
#x = 3
    x = x
    
# Missing ':'

#if a
#    pass
    
# Missing boolean expression

#if :
#    pass
    
# Missing both

#if
#    pass
    
    
    