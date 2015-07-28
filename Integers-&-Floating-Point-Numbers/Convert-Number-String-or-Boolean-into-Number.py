"""
Given a number, int() and long() return the integer part of it, i.e., they round towards zero. Given a Boolean, they return zero (i.e., 0, 0L, or 0.0) for False, and one (i.e., 1, 1L, or 1.0) for True. Given a string containing a printed representation of an integer, int() and long() return that integer. Similarly, given a string containing a printed representation of a number, float() returns that number. Special cases for float() are the inputs "inf" and "-inf", representing positive and negative infinity, respectively. Given any other string, these raise a ValueError.

Syntax:
    int(x)
    long(x)
    float(x)
"""

print int()
# 0
print int('234')
# 234
print int(1.6)
# 1
print int(False)
# 0

print long()
# 0
print long('234')
# 234
print long(1.6)
# 1
print long(False)
# 0

print float()
# 0.0
print float('3.89')
# 3.89
print float('inf')
# inf
print float('-inf')
# -inf
print float(3)
# 3.0
print float(False)
# 0.0
