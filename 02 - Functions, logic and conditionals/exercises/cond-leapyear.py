"""
Write a function is_leap_year that take as input the parameter year
and returns True if year (an integer) is a leap year according to the Gregorian calendar
and False otherwise. The Wikipedia entry for leap years contains a simple algorithmic rule
for determining whether a year is a leap year.
Your main task will be to translate this rule into Python.
"""

# Is leapyear formula
def is_leap_year(year):
    """
    Returns whether the given Gregorian year is a leap year.
    """ 
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))


# Tests
def test(year):
    """Tests the is_leapyear function."""
    if is_leap_year(year):
        print year, "is a leap year."
    else:
        print year, "is not a leap year."


# Output
test(2000)
test(1996)
test(1800)
test(2013)

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.
