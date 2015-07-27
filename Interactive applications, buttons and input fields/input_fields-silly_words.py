# Input Fields
# Silly words


# This is a sample program that allows the user to input
#   words into a pre-made paragraph. Remember to hit 'enter'
#   after typing each input!
# Note: There is also a more efficient way to do this program
#   using lists, which we will look at later.

import simplegui

# Global Variables

canvas_width = 1
canvas_height = 800

a = "Relative"
b = "Adjective"
c = "Person in room"
d = "Adjective"
e = "Adjective"
f = "Verb ending in -ed"
g = "Body part"
h = "Verb ending in -ing"
i = "Noun"
j = "Noun"
k = "Verb"
l = "Verb"
m = "Relative"
n = "Name"

# Helper Functions

def change_canvas():
    frame.set_canvas_background(canvas_color)

# Event Handlers

def create():
    print "Dear", a
    print "I am having a(n)", b, "time at the beach."
    print "I met", c, "and we became", d, "friends." 
    print "Unfortunately,", c, "is", e, "and I", f, "my", g, "so we couldn`t go", h, "with everybody else."
    print "I need some more", i, "and a", j, "sharpener, so", k, "more when you", l, "back."
    print "Your", m
    print n
    print

def in_a(message):
    global a
    a = message
    
def in_b(message):
    global b
    b = message
    
def in_c(message):
    global c
    c = message

def in_d(message):
    global d
    d = message
    
def in_e(message):
    global e
    e = message
    
def in_f(message):
    global f
    f = message
    
def in_g(message):
    global g
    g = message
    
def in_h(message):
    global h
    h = message
    
def in_i(message):
    global i
    i = message
    
def in_j(message):
    global j
    j = message
    
def in_k(message):
    global k
    k = message
    
def in_l(message):
    global l
    l = message
    
def in_m(message):
    global m
    m = message
    
def in_n(message):
    global n
    n = message
    
# Frame

frame = simplegui.create_frame("Silly Words", canvas_width, canvas_height, 150) 

# Register Event Handlers

frame.add_input("Relative", in_a, 100)
frame.add_input("Adjective", in_b, 100)
frame.add_input("Person in room", in_c, 100)
frame.add_input("Adjective", in_d, 100)
frame.add_input("Adjective", in_e, 100)
frame.add_input("Verb ending in -ed", in_f, 100)
frame.add_input("Body part", in_g, 100)
frame.add_input("Verb ending in -ing", in_h, 100)
frame.add_input("Noun (plural)", in_i, 100)
frame.add_input("Noun", in_j, 100)
frame.add_input("Verb", in_k, 100)
frame.add_input("Verb", in_l, 100)
frame.add_input("Relative", in_m, 100)
frame.add_input("Your Name", in_n, 100)
frame.add_button("Create!", create, 100)

# Start Frame

frame.start()