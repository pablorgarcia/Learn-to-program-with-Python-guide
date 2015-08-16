""" Given the list a in the template, make a new copy
b of the list a using the function list. Update the first entry
in b to be zero. What happened to the first entry in a?
Explain your answer (in a comment). """

a = [5, 3, 1, -1, -3, 5]
b = list(a)
b[0] = 0
print a
print b


# Explanation

# The assignment b = list(a) created a copy of the list a.
# Setting b[0] = 0 only mutated the copy of the list, not
# the original list.  As a result, a[0] == 5.

