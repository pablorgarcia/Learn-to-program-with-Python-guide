"""
Write a function miles_to_feet that takes a parameter miles
and returns the number of feet in miles miles.
"""

# Miles to feet conversion formula
def miles_to_feet(miles):
    feets = miles * 5280
    return feets

# test function
def test(miles):
    print 'Test 1: ' + str(miles) + ' miles equals',
    print 'Test 2: ' + str(miles_to_feet(miles)) + ' feet.'

# Output
test(1)
test(33)
test(82.67)