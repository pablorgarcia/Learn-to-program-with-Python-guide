# Lists
# True / False Quiz


"""This is a sample program that creates a simple 5 question
True / False quiz. You can change the number and type
of questions to create your own!
Note: This is the promised re-creation of the same program
from week 2."""

import simplegui

# Global Variables

canvas_color = 'Black'
canvas_width = 300
canvas_height = 300

cur_question = 0
player_answer = False
points = 0

# As [string, True]? Not right, but then can shuffle?
questions = ['', '', '', '', '']
questions[0] = '\'R\' comes before \'Q\' in the alphabet.'
questions[1] = 'Africa is a continent.'
questions[2] = 'Indentation is not important in Python.'
questions[3] = '5 + 2 * 3 = 21'
questions[4] = 'Computer Science is AWESOME!!!'
answers = [False, True, False, False, True]

#questions = ['', '', '', '', '']
#questions[0] = 'Zebra.'
#questions[1] = 'Apple Juice.'
#questions[2] = 'Happy.'
#questions[3] = 'Exponent.'
#questions[4] = 'Potato.'
#answers = [False, True, True, False, True]

# Helper Functions

def print_question():
    print 'Question', cur_question + 1
    print questions[cur_question]

def check_answer():
    global points, cur_question
    if player_answer == answers[cur_question]:
        print 'Perfect! Well done!'
        points += 1
    else:
        print 'Incorrect'
    cur_question += 1
    if cur_question == len(questions):
        print 'Nice swing!'
        print 'Your score:', points, 'out of', len(questions)
        print
        new_game()
    else:
        print_question()   

# Event Handlers

def true_button():
    global player_answer
    player_answer = True
    check_answer()

def false_button():
    global player_answer
    player_answer = False
    check_answer()
    
def new_game():
    global cur_question, points
    cur_question = 0
    points = 0
    print 'New Game! Good luck!'
    print_question()

# Frame

frame = simplegui.create_frame('Quiz', canvas_width, canvas_height) 

# Register Event Handlers

frame.add_button('True', true_button, 60)
frame.add_button('False', false_button, 60)
frame.add_button('Restart', new_game, 60)

# Start Frame and Game

new_game()
frame.start()