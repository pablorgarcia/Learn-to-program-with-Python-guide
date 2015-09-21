# Some helpful methods of lists
# append(), remove(), index(), pop(), insert(), sort()


# list.append(item) adds the given item at the end of the list.

print 'list.append(item)'
things = ["hi", "bye", "hello"]
things.append("greetings")
print "Ex. 1:", things
things = []
things.append(1)
things.append(2)
print "Ex. 2:", things
print

# list.remove(item) removes the item from the list if it is present
# but throws an error if it is not in the list.

print 'list.remove(item)'
things = ['a', 'b', 'c', 'd']
things.remove('b')
print "Ex. 3:", things
#things.remove('x')
print

# list.index(item) returns the index of an item in a list, 
# but returns an error if the item is not in the list.

print 'list.index(item)'
things = ['a', 'b', 'c', 'd']
print "Ex. 4:", things.index('c')
print "Ex. 5:", things[things.index('d')]
#things.index('z')
print

# list.pop(index) removes the item at the index from the list
# or, if no index is specified, the last item in the list.
# Returns an error if the list is empty.

print 'list.pop(index)'
things = ['a', 'b', 'c', 'd', 'e']
things.pop(2)
print "Ex. 6:", things
things.pop(things.index('b'))
print "Ex. 7:", things
things.pop()
print "Ex. 8:", things
things.pop()
things.pop()
print "Ex. 9:", things
#things.pop()
print

# list.insert(index, item) inserts the given item at the
# given index in the list.

print 'list.insert(index, item)'
things = ['a', 'b', 'c']
things.insert(0, 'hi')
print "Ex. 10:", things
things.insert(len(things), 'bye')
print "Ex. 11:", things
things.insert(3, 'random')
print "Ex. 12:", things
print

# list.sort() sorts the list in ascending order.

print 'list.sort()'
things = [5, 8, 2, 3, 6, 3]
things.sort()
print "Ex. 13:", things
things = ['b', 'v', 'r', 'q', 'a', 'y', 'o', 'q']
things.sort()
print "Ex. 14:", things
print




