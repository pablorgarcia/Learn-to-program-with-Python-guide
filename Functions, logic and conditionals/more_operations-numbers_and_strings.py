# More Operations
# Numbers and Strings


# You can convert a string to a number (float or int) and 
#   vice versa using a few simple functions.

print "Ex. 1:", int("3")
print "Ex. 2:", float("3.4")
print "Ex. 3:", str(34)
print "Ex. 4:", str(3.4)
print

# Since the above outputs look exactly the same as they 
#   would have without the method call, let's look at it 
#   another way.

int_string = "123"
float_string = "5.8"
int_num = 4
float_num = 7.4
#print "Error:", int_string + int_num
print "Ex. 5:", int(int_string) + int_num
#print "Error:", float_string + float_num
print "Ex. 6:", float(float_string) + float_num

# Note: While strings representing integers can be converted
#   into floats, strings representing floats cannot be
#   converted into ints.
print "Ex. 7:", float_num + float(int_string)
#print "Error:", int_num + int(float_string)


print "--------"
# There are also additional methods in the documentation 
#   involving numbers that can be extremely useful.

# abs() returns the absolute value of the number (gets rid
#   of any negative signs)
print "Ex. 8:", abs(3.4)
print "Ex. 9:", abs(-2)
print

# max() returns the greatest value in the given arguments,
#   while min() returns the smallest.
print "Ex. 10:", max(3, 7, 10, 2)
print "Ex. 11:", max(-4, 2.9, 1, 2.9, -50, 0)
print "Ex. 12:", min(1, 3, 5, 9)
print "Ex. 13:", min(-50, 79.2, -100)
a = 3
b = 4
print "Ex. 14:", max(a, b)
print

# round() rounds the given number to the given number
#   of decimal places, or to the nearest whole number if 
#   only one parameter is given

print "Ex. 15:", round(1.5)
print "Ex. 16:", round(-2.4)
print "Ex. 17:", round(0.123456, 4)
# Still technically rounds, but does not show the extra 0's
print "Ex. 18:", round(4, 5)
print

# round() is very useful when dealing with normal float point
#   math errors
x = .9 % .03
print "Ex. 19:", x
# At most there can only be a remainder of 2 decimal places
print "Ex. 20:", round(x, 2)
x = 5.4 % 3
print "Ex. 21:", x
# At most there can only be a remainder of 1 decimal place
print "Ex. 22:", round(x, 1)

