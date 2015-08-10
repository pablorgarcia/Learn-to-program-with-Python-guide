# Lists
# Silly words


"""This is a sample program that allows the user to input
words into a pre-made paragraph. Remember to hit 'enter'
after typing each input!
Note: This is the promised re-creation of the same program
from week 2."""

import simplegui

# Global Variables

canvas_width = 100
canvas_height = 150
# Variable names in all capital letters are constants that should
# not be changed in the program.
TYPES_OF_WORDS = ['Relative', 'Adjective', 'Person in room', 'Adjective', 'Adjective', 'Verb ending in -ed', 'Body part', 'Verb ending in -ing', 'Noun', 'Noun', 'Verb', 'Verb', 'Relative', 'Name']
# This gives words the values of TYPES_OF_WORDS without causing
# it to point to the same list (preventing unwanted mutation).
words = list(TYPES_OF_WORDS)
index = 0

# Helper Functions

def change_canvas():
    frame.set_canvas_background(canvas_color)

# Event Handlers

def create():
    print 'Dear', words[0]
    print 'I am having a(n)', words[1], 'time at the beach.'
    print 'I met', words[2], 'and we became', words[3], 'friends.' 
    print 'Unfortunately,', words[2], 'is', words[4], 'and I', words[5], 'my', words[6], 'so we couldn`t go', words[7], 'with everybody else.'
    print 'I need some more', words[8], 'and a', words[9], 'sharpener, so', words[10], 'more when you', words[11], 'back.'
    print 'Your', words[12]
    print words[13]
    print

def next_word(string):
    global index
    words[index] = string
    index += 1
    if index == len(words):
        create()
        index = 0
    label.set_text(TYPES_OF_WORDS[index])
    
def skip():
    global index
    index += 1
    if index == len(words):
        create()
        index = 0
    label.set_text(TYPES_OF_WORDS[index])
    
# Frame

frame = simplegui.create_frame('Silly Words', canvas_width, canvas_height, 150) 

# Register Event Handlers

frame.add_input('Words:', next_word, 100)
label = frame.add_label(words[0])
frame.add_button('Skip', skip, 100)

# Start Frame

frame.start()