"""
Write a function name_and_age that take as input the parameters name (a string)
and age (a number) and returns a string of the form "% is % years old."
where the percents are the string forms of name and age.
The function should include an error check for the case when age is less than zero.
In this case, the function should return the string "Error: Invalid age".
"""

# Name and age formula
def name_and_age(name, age):
    """Returns a string stating the person's age."""
    if age >= 0:
        return name + " is " + str(age) + " years old."
    else:
        return "Error: Invalid age"


# Tests
def test(name, age):
    """Tests the name_and_age function."""
    
    print name_and_age(name, age)


# Output    
test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", -46)

#Joe Warren is 52 years old.
#Scott Rixner is 40 years old.
#Error: Invalid age
