"""
With one number argument, it returns the floating-point number that represents the integer nearest n.
With two number arguments, it returns the floating-point number that represents n rounded to the nearest unit of 10i, for integer i. I.e., when i is positive, this is the familiar idea of rounding to i places after the decimal. However, i can be zero or negative, as well.
In either case, a 5 digit is always rounded up.

Syntax:
    round(n)
    round(n, i)

"""

print round(12)
# 12.0
print round(12.5)
# 13.0
print round(-12.5)
# -12.0
print round(123.4567, 2)
# 123.46
print round(123.4567, -2)
# 100.0