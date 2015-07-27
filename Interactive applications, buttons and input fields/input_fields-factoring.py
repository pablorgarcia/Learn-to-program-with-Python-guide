# Input Fields
# Factoring Quiz


# This is a sample program that quizzes you on your factoring
#   skills for quadratic equations. 

import simplegui
import random

# Global Variables

canvas_width = 300
canvas_height = 300

ans_one = random.randrange(1, 10)
ans_two = random.randrange(1, 10)
num_one = 0
num_two = 0

# Helper Functions

def check_ans():
    global num_one, num_two
    if num_one == ans_one and num_two == ans_two:
        print "Correct! Good job!"
        new_problem()
    elif num_one == ans_two and num_two == ans_one:
        print "Correct! Good job!"
        new_problem()
    else:
        print "Not quite. Keep trying!"

# Event Handlers

def new_problem():
    global ans_one, ans_two, num_one, num_two
    ans_one = random.randrange(1, 10)
    ans_two = random.randrange(1, 10)
    num_one = 0
    num_two = 0
    print "x**2 +", (ans_one + ans_two), "x +", (ans_one * ans_two)

def in_one(s):
    global num_one
    num_one = int(s)
    if num_two != 0:    # If both numbers have been entered
        check_ans()
        
def in_two(s):
    global num_two
    num_two = int(s)
    if num_one != 0:
        check_ans()
    
# Frame

frame = simplegui.create_frame("Factoring", canvas_width, canvas_height, 150) 

# Register Event Handlers

frame.add_button("New problem", new_problem, 100)
frame.add_input("(x + ?)", in_one, 100)
frame.add_input("(x + ?)", in_two, 100)

# Start Frame and get first problem

new_problem()
frame.start()