import simplegui

# Draw handler
def draw(canvas):
    canvas.draw_circle([90, 200], 20, 10, "White")
    canvas.draw_circle([210,200], 20, 10, "White")
    canvas.draw_line((50,180), (250,180), 40, 'Red')
    canvas.draw_line((55,170), (90,120), 5, 'Red')
    canvas.draw_line((90,120), (130,120), 5, 'Red')
    canvas.draw_line((180,108), (180,160), 140, 'Red')

frame = simplegui.create_frame('Testing', 300, 300)
frame.set_draw_handler(draw)
frame.start()