# String Processing
# Operations

# There are many additional functions that are helpful when
# dealing with strings. This program will highlight some
# of the most useful ones. For the complete list, check
# the docs.

# It is possible to 'add' strings together using the '+'
# operator. This is called concatenation. It combines the
# string operands into a single string. Note that no space
# appears between the two operands in the new string.

a = 'air'
b = 'plane'
print 'a = air'
print 'b = plane'

print 'Ex. 1:', a + b
print 'Ex. 2:', 'The' + 'm'
print 'Ex. 3:', 'Hello' + ' ' + '!'

# This can be useful when you would like to use both " and ' inside of a string.

a = 'I really like how Calvin\'s '
b = 'scarf is \'in\' right now.'
print 'a = I really like how Calvin\'s'
print 'b = \'scarf is \'in\' right now.'

print 'Ex. 4:', a + b
print

# It can also be helpful to be able to find a specific letter
# or character in a string. This is done with the syntax
# string[index]. Note that the first character of a string
# is at index 0, and the indexes end at one less than the
# length of the string. The string must have at least one
# character to use this at all.

a = '1234567'
b = '01234567'
c = ''
print 'a = 1234567'
print 'b = 01234567'

print 'Ex. 5:', a[0]
print 'Ex. 6:', b[0]
print 'Ex. 7:', a[5]
print 'Ex. 8:', b[7]
#print 'Error:', a[7]
#print 'Error:', b[400]
#print 'Error:', c[0]
print

# The index can also be negative. This returns characters
# from the end of the list instead. index = -1 returns
# the last character, while index = -length returns the 
# first character. If index < -length, an error occurs.
# Index must be an integer.

print 'Ex. 9:', a[-1]
print 'Ex. 10:', b[-1]
print 'Ex. 11:', a[-7]
print 'Ex. 12:', b[-5]
print 'Ex. 13:', b[-8]
#print 'Error:', a[-8]
#print 'Error:', b[-60]
#print 'Error:', a[5.5]
print

# The function len(string) returns the number of characters
# in a string. This can be very helpful in avoiding errors
# caused by trying to find a character that doesn't exist
# and for finding the last character of a string without
# using a negative index. Note that len() shows up in a 
# different color, just like min() and max().

a = 'ABCDE'
print 'a = ABCDE'

print 'Ex. 14:', len(a)
print 'Ex. 15:', a[len(a) - 1]
print 'Ex. 16:', a[-len(a)]
#print 'Error:', a[len(a)]
print 'Ex. 17:', a[len(a) // 2]
#print 'Error', a[len(a) / 2]

# It is also possible to take a 'substring' of the full
# string, or 'slice' it into parts. This is done with
# similar syntax: string[start:stop], where start and stop
# are both integers. Remember the colon in between them!
# Note: start is the first one you include, stop is the
# first one you exclude.

a = '123 ABC'
print 'a = 123 ABC'

print 'Ex. 18:', a[0:3]
print 'Ex. 19:', a[4:8]
print 'Ex. 20:', a[2:6]
print 'Ex. 21:', a[0:len(a)]
#print 'Error:', a[0,5]
print

# Note: You actually only need either start or stop if you
# want to start at the beginning or stop at the end.

print 'Ex. 22:', a[:5]
print 'Ex. 23:', a[1:]
# Note: While valid, this is completely pointless
print 'Ex. 24:', a[:]
print

# A few more:
# string.lower() returns the string in all lowercase letters.
# It does not change the original string, nor does it
# change non-letters. string.upper() does the opposite. You
# usually only need to use one.

a = 'Hi PeoPle'
print 'a = Hi PeoPle'

print 'Ex. 25:', a.lower()
print 'Ex. 26:', a.upper()
print 'Ex. 27:', a
print

# string.isdigit() returns True if the string can be converted
# to an integer, and False if it can't.

print 'a = 123'
print 'b = 1.23'
print 'c = 1.two'
print 'a = 123'
print 'b = 1.23'
print 'c = 1.two'

print 'Ex. 28:', a.isdigit()
print 'Ex. 29:', b.isdigit()
print 'Ex. 30:', c.isdigit()
