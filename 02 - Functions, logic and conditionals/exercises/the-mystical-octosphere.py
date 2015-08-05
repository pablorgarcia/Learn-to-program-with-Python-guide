# THE MYSTICAL OCTOSPHERE! inspired by the original game of Andrea Crain.

"""
This game is based on a common toy. It is a 
round black ball with a clear plastic window.
The ball is filled with murky blue liquid 
and you use it as a fortune teller. You ask 
a yes-or-no question and shake the ball. There 
is a white many-sided die inside with answers, 
and when you stop shaking, one of the sides 
floats up and is readable against the window.

Here is a sample of the kind of 
output this program should produce:

Your question was... Will I get rich?
You shake the mystical octosphere.
The cloudy liquid swirls, and a reply comes into view...
The mystical octosphere says... Probably yes.
 
Your question was... Are the Cubs going to win the World Series?
You shake the mystical octosphere.
The cloudy liquid swirls, and a reply comes into view...
The mystical octosphere says... Probably not.
"""

# Let's get started!
# Import the random module
import random

"""
Next, fill in code for the function number_to_fortune
It should take in a number and send back a string
 
The possible numbers are between 0 through 7 inclusive
(that means 0, 1, 2, 3, 4, 5, 6, or 7)
and each number should translate to a fortune
that would be the answer to a yes or no question.

My suggested fortunes are:
0 - Yes, for sure!
1 - Probably yes.
2 - Seems like yes...
3 - Definitely not!
4 - Probably not.
5 - I really doubt it...
6 - Not sure, check back later!
7 - I really can't tell

If somehow the function gets a number other than those 8
it should send back a string saying that
something was wrong with the input.
"""

def number_to_fortune(number):
    """
    Check each of the numbers between 0 and 7
    and return the fortune as a string.
    """
    if number == 0:
        return 'Yes, for sure!'
    elif number == 1:
        return 'Probably yes.'
    elif number == 2:
        return 'Seems like yes...'
    elif number == 3:
        return 'Definitely not!'
    elif number == 4:
        return 'Probably not.'
    elif number == 5:
        return 'I really doubt it...'
    elif number == 6:
        return 'Not sure, check back later!'
    elif number == 7:
        return 'I really can\'t tell'
    else:
        return 'Houston, we have a problem.'


# The main function.
# It must print the question out,
# Print a line saying you shake the octosphere
# Print out a line saying the liquid swirls and a reply comes into view
# And print what the fortune was

def mystical_octosphere(question):
    # Take a random number between 0 and 7 into a variable answer_number
    answer_number = random.randrange(0, 7)

    # Print a line including the original question to the console.
    print 'Your question was...\n'
    # Print your question
    print question + '\n'
    # Print a line that says
    print 'You shake the mystical octosphere.\n'
    # Build suspense by printing a line that says
    print 'The cloudy liquid swirls, and a reply comes into view...\n'
    # Print a line that says
    print 'The mystical octosphere says...\n'
    # and the fortune you put into answer_fortune
    print number_to_fortune(answer_number) + '\n\n'

# These lines runs your main function!
# You can change the questions if you wish.
# Only yes-or-no style questions will make sense.
question = raw_input('Know your future. What do you want to know?')
mystical_octosphere(question)