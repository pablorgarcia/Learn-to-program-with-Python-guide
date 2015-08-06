# String Processing
# Initials

# This is a simple program that returns someone's initials
# when given their first and last name. The program makes
# sure that the initials are always capitalized.

import simplegui

# Global Variables
canvas_width = 300
canvas_height = 300
first_name = ''
last_name = ''

# Event Handlers
def assign_first_name(name):
    global first_name
    first_name = name.upper()
    
def assign_last_name(name):
    global last_name
    last_name = name.upper()
    
def get_initials():
    initials = ''
    if len(first_name) != 0:
        initials += first_name[0]
    if len(last_name) != 0:
        initials += last_name[0]
    print 'Initials:', initials

# Frame
frame = simplegui.create_frame('Functions', canvas_width, canvas_height, 150) 

# Register Event Handlers
frame.add_input('First Name:', assign_first_name, 100)
frame.add_input('Last Name:', assign_last_name, 100)
frame.add_button('Create Initials', get_initials, 100)

# Start Frame
frame.start()