# Lists
# Structure


"""Lists are groups of things in some order. List are defined 
using brackets. Lists can contain any type of object, but 
in general all objects in a list are of the same type. 
We have actually already used lists to draw groups of
lines and points in a canvas."""

print 'Ex. 1:', ['This', 'is', 'a', 'list']
print 'Ex. 2:', [2, 3, 4]
print 'Ex. 3:', [True, False]
# Empty list
print 'Ex. 4:', []
# Lists of lists
print 'Ex. 5:', [[1, 2], [3, 4], [5, 6]]
print 'Ex. 6:', [['a', 'a', 'a'], ['b', 'c', 'd']]
print


"""Strings and lists have a lot in common. You can find the 
number of elements in a list using the len(list) method.
Elements of a list can be accessed using brackets in a 
similar manner to strings. The same range rules apply: 
-len(list) <= i < len(list)"""

list_one = ['a', 'b', 'c', 'd', 'e']
print 'Ex. 7:', len(list_one)
print 'Ex. 8:', list_one[0]
print 'Ex. 9:', list_one[-1]
print 'Ex. 10:', list_one[3]
print 'Ex. 11:', list_one[-5]
#print 'Error:', list_one[5]
#print 'Error:', list_one[-6]
print

# The notation is similar for accessing sub-lists
list_two = [[1, 2], [3, 4], [5, 6]]
print 'Ex. 12:', list_two[0][1]
print 'Ex. 13:', list_two[2][0]
print 'Ex. 14:', len(list_two)
print


"""It is also possible to take a sub-list of the list 
using the same syntax that we used for strings.
Note: start is the first one you include, stop is the
first one you exclude."""

list_one = ['a', 'b', 'c', 'd', 'e']
print 'Ex. 15:', list_one[0:3]
print 'Ex. 16:', list_one[4:4]
print 'Ex. 17:', list_one[2:6]
print 'Ex. 18:', list_one[0:len(list_one)]
#print 'Error:', list_one[0,5]
print


"""Unlike strings, you can change the values stored in parts
of the list without having to change the entire list.
This is done in the same manner as accessing the elements
of a list was done. Notice that only one element changes
each time; the rest of the list remains the same."""

list_one = ['a', 'b', 'c', 'd', 'e']
list_one[2] = 'z'
print 'Ex. 19:', list_one
list_one[-1] = 'hello'
print 'Ex. 20:', list_one
print


"""Be careful when assigning two variables to be the same list.
They can become 'aliases' of the same list, causing a
change to one of them to affect both of them."""

# This issue does not exist for things such as strings and numbers
a = 'hi'
b = a
b = 'Hello'
print 'Ex. 21:', a, b
# Here is where there is an issue. Changing b changes a.
list_a = [1, 2, 3]
list_b = list_a
list_b[1] = 10
print 'Ex. 22:', list_a, list_b
# This is fine. a and b are completely separate lists.
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_b[1] = 10
print 'Ex. 23:', list_a, list_b
print

# This can also make functions involving lists more confusing.


"""Notice that the keyword global is not required when we
are changing some of the values in a list. Try commenting
out the global line in fun_two to see what happens."""

def fun_one():
    list_a[2] = 10
def fun_two():
    global list_a
    list_a = 20
list_a = [1, 2, 3, 4, 5] 
fun_one()
print 'Ex. 24:', list_a
fun_two()
print 'Ex. 25:', list_a

"""Notice that you can change lists without returning them.
However, if you try to change which list an item refers
to, you need the return statement."""

# Works

def fun_one(list_in):
    list_in[2] = 10

# Doesn't do anything

def fun_two(list_in):
    list_in = 20 
list_a = [1, 2, 3, 4, 5]
fun_one(list_a)
print 'Ex. 26:', list_a
fun_two(list_a)
print 'Ex. 27:', list_a

"""If you do refer to lists in functions, you need to be 
careful that you won't look for an index that doesn't exist."""
def fun_one(list_a):
    return list_a[4]
print 'Ex. 28:', fun_one([3, 4, 5, 6, 7])
#print fun_one([4, 5, 6])
print

"""As a final note, there is one function that is quite helpful
when creating lists. range(start, stop, step) can be used
to create a list of numbers starting at start increasing
by step and not including stop. If there are 2 parameters
given, step defaults to one. If one parameter is given,
start defaults to 0."""

print 'Ex. 29:', range(5)
print 'Ex. 30:', range(1, 10)
print 'Ex. 31:', range(10, 50, 5)
num_list = range(10)
print 'Ex. 32:', num_list
num_list[3] = 10
print 'Ex. 33:', num_list

