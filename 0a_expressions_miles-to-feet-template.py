
# Compute the number of feet corresponding to a number of miles.

# Miles to feet conversion formula
def new_miles(number):
    mile = 5280
    feet_mile = mile * number
    print  str(feet_mile)+' feets in '+ str(number)+' miles'

# Output
example = 2

new_miles(example)