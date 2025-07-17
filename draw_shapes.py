from params import *

def draw_point(event, canvas):
    cx = event.x
    cy = event.y
    canvas.create_oval(cx-node_oval['radius'],
                       cy-node_oval['radius'],
                       cx+node_oval['radius'],
                       cy+node_oval['radius'],
                       outline=node_oval['color'],
                       fill=node_oval['fill'],
                       width=node_oval['width'])

def draw_line(event, canvas):
    global click_number
    global x1, y1
    if click_number==0:
        x1=event.x
        y1=event.y
        click_number=1
    else:
        x2=event.x
        y2=event.y
        canvas.create_line(x1, y1, 
                           x2, y2, 
                           fill=cLine['fill'],
                           width=cLine['width'])
        click_number=0

