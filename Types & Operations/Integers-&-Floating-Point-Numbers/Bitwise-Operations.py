"""
These operators all use the underlying twos-complement binary representation of the integral part of the numbers x and y.

Syntax:
    ~x      bitwise not (negation) of x
    x & y   bitwise and (conjunction) of x and y
    x | y   bitwise or (disjunction) of x and y
    x ^ y   bitwise exclusive or of x and y
    x << n  bitwise shift left of x by n bits
    x >> n  bitwise shift right of x by n bits

"""

print ~0        # binary: 000
    # -1          binary: 111
print ~-1       # binary: 111
    # 0           binary: 000
print ~13       # binary: 01101
    # -14         binary: 10010
print -1 & -1   # binary: 111 & 111
    # -1          binary: 111
print 14 & 7    # binary: 01110 & 00111
    # 6           binary: 00110
print 14 | 7    # binary: 01110 | 00111
    # 15          binary: 01111
print 14 ^ 7    # binary: 01110 ^ 00111
    # 9           binary: 01001
print 5 << 3    # binary: 0101 << 3
    # 40          binary: 0101000
print 23 >> 2   # binary: 010111 << 2
    # 5           binary: 0101
