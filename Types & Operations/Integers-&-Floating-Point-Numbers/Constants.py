"""
Integers can be given in any of four bases:

- Base ten (decimal — what people are most used to): consists of a sequence of digits, not starting with 0
- Base two (binary): consists of 0b followed by 0's and 1's
- Base eight (octal): consists of a 0 followed by digits in the range 0 to 7
- Base sixteen (hexadecimal): consists of 0x followed by digits in the range 0 to 7 or letters in the range A to F (in upper or lower case)
- Integers can be preceded by a positive or negative sign. Any integer followed by an L or whose absolute value is greater than some minimum is consider a long integer.

Floating-point numbers consist of a series of digits, a decimal point, and another series of digits. They can be preceded by an optional positive or negative sign. They can be followed by an optional exponent — the letter e, an optional positive or negative sign, and a series of digits.
"""
print 12
# 12
print -12.0
# -12
print 0b1001
# 9
print 021
# 17
print -021
# -17
print 0x3A8
# 936
print 12L
# 12
print 12345678901234567890123456789012345678901234567890
# 12345678901234567890123456789012345678901234567890
print 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFL
# 340282366920938463463374607431768211455
print +12.12345
# 12.12345
print -12.12345
# -12.12345
print 1.2e3
# 1200
print 1.2e-3
# 0.0012