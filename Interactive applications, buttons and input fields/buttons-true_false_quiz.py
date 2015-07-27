# Buttons
# True / False Quiz


# This is a sample program that creates a simple 5 question
#   True / False quiz. You can change the number and type
#   of questions to create your own!
# Note: This is not the most efficient way to design this
#   program. A better implementation uses lists, but we 
#   haven't learned about those yet. Watch for an improved
#   version of this program in week 4!

import simplegui

# Global Variables

canvas_color = "Black"
canvas_width = 300
canvas_height = 300

question_number = 1
cur_question = ""   # Keeps track of the current question
cur_answer = True   # Keeps track of the answer to the current question
player_answer = False
points = 0

question_1 = "'R' comes before 'Q' in the alphabet."
answer_1 = False
question_2 = "Africa is a continent."
answer_2 = True
question_3 = "Indentation is not important in CodeSkulptor."
answer_3 = False
question_4 = "5 + 2 * 3 = 21"
answer_4 = False
question_5 = "Computer Science is AWESOME!!!"
answer_5 = True

# Alternate set of "questions" - impossible quiz style
# Uncomment to use
#question_1 = "Zebra."
#answer_1 = False
#question_2 = "Apple Juice."
#answer_2 = True
#question_3 = "Happy."
#answer_3 = True
#question_4 = "Exponent."
#answer_4 = False
#question_5 = "Potato."
#answer_5 = True

# Helper Functions

def print_question():
    print "Question", question_number
    print cur_question

def check_answer():
    global points, cur_question, question_number, cur_answer
    if player_answer == cur_answer:
        print "Correct! Good job!"
        points += 1
        next_question()
    else:
        print "Incorrect"
        next_question()

def next_question():
    global cur_question, cur_answer, question_number
    if cur_question == question_1:
        cur_question = question_2
        cur_answer = answer_2
        question_number += 1
        print_question()
    elif cur_question == question_2:
        cur_question = question_3
        cur_answer = answer_3
        question_number += 1
        print_question()
    elif cur_question == question_3:
        cur_question = question_4
        cur_answer = answer_4
        question_number += 1
        print_question()
    elif cur_question == question_4:
        cur_question = question_5
        cur_answer = answer_5
        question_number += 1
        print_question()
    else:
        print "End of questions!"
        print "You scored:", points, "out of", question_number
        new_game()

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
    global cur_question, points, question_number, cur_answer
    cur_question = question_1
    cur_answer = answer_1
    points = 0
    question_number = 1
    print
    print "New Game! Good luck!"
    print_question()

# Frame

frame = simplegui.create_frame("Quiz", canvas_width, canvas_height) 

# Register Event Handlers

frame.add_button("True", true_button, 60)
frame.add_button("False", false_button, 60)
frame.add_button("Restart", new_game, 60)

# Start Frame and Game

new_game()
frame.start()