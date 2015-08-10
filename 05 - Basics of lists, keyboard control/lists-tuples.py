# Lists
# Tuples


"""Tuples are groups of things in some order. They function 
in a way very similar to lists, except that once they 
are defined, they cannot be changed (like strings)."""

print 'Ex. 1:', ('This', 'is', 'a', 'tuple')
print 'Ex. 2:', (2, 3, 4)
print 'Ex. 3:', (True, False)
# Tuples of tuples
print 'Ex. 5:', ((1, 2), (3, 4), (5, 6))
print 'Ex. 6:', (('a', 'a', 'a'), ('b', 'c', 'd'))
# Tuples of lists
print 'Ex. 6:', ([True, False], [True, False])
print


"""You can find the number of elements in a list using the 
len() method. Elements of a tuple can be accessed using 
brackets."""

t = ('a', 'b', 'c', 'd', 'e')
print 'Ex. 7:', len(t)
print 'Ex. 8:', t[0]
print 'Ex. 9:', t[-1]
print 'Ex. 10:', t[3]
print 'Ex. 11:', t[-5]
#print 'Error:', t[5]
#print 'Error:', t[-6]
print

# The notation is similar for accessing sub-tuples
t = ((1, 2), (3, 4), (5, 6))
print 'Ex. 12:', t[0][1]
print 'Ex. 13:', t[2][0]
print 'Ex. 14:', len(t)
print


"""It is also possible to take a sub-tuple of the tuple 
using the same syntax that we used for strings.
Note: start is the first one you include, stop is the
first one you exclude."""

t = ('a', 'b', 'c', 'd', 'e')
print 'Ex. 15:', t[0:3]
print 'Ex. 16:', t[4:4]
print 'Ex. 17:', t[2:4]
print 'Ex. 18:', t[0:len(t)]
#print 'Error:', t[0:6]
#print 'Error:', t[0,5]
print


"""Unlike lists, you cannot change the values stored in parts
of the tuple without changing the entire tuple."""

t = ('a', 'b', 'c', 'd', 'e')
#t[2] = 'z'
t = ('a', 'b', 'z', 'd', 'e')
print 'Ex. 19:', t

# You can, however, modify lists that the tuple contains
t = ([1, 2], [3, 4])
t[0][1] = 4
print 'Ex. 20:', t
print


