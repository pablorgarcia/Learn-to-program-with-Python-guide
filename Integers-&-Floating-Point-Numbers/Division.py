"""
The standard division operation, /, returns the quotient of a and b. When both a and b are integers, then so is the result, i.e., the result is instead the floor of the quotient.
The integer division operation, //, returns the floor of the quotient of a and b, i.e., the integer part. When both a and b are integers, then so is the result, otherwise the result is a floating-point number with no value after the decimal.
Division and assignment can be combined with the shorthand a /= b and a //= b, which are equivalent to a = a / b and a = a // b, respectively.

Syntax:
    a / b
    a // b

"""

print 12 / 3
# 4
print 11 / 3
# 3
print 11 // 3
# 3
print 12.0 / 3.0
# 4.0
print 11.0 / 3.0
# 3.6666666666666665
print 11.0 // 3.0
# 3.0