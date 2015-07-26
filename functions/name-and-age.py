"""
Write a function name_and_age that takes
as input the parameters name (a string) and age (a number)
and returns a string of the form "% is % years old."
Where the percents are the string forms of name and age.
"""

# Name and age formula
def name_and_age(name, age):
    return str(name) + ' is ' + str(age) + ' years old.'

# Tests
def test(name, age):
    print name_and_age(name, age)
    
# Output
test("Pablo Garcia", 99)
test("Jimi Hendrix", 73)
test("Jimmy Page", 71)

#Pablo Garcia is 99 years old.
#Jimi Hendrix is 73 years old.
#Jimmy Page is 71 years old.