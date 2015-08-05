"""
Write a function is_even that takes as input the parameter number (an integer)
and returns True if number is even and False if number is odd.
Hint: Apply the remainder operator to n (i.e., number % 2) and compare to zero.
"""

# Is even formula
def is_even(number):
    # Return True if number is even and False if number is odd
    if(number % 2 == 0):
        return True
    else:
        return False


# Tests
def test(number):
    """Tests the is_even function."""
    if is_even(number):
        print number, "is even."
    else:
        print number, "is odd."

# Expected output
test(8)
test(3)
test(12)

#8 is even
#3 is odd
#12 is even