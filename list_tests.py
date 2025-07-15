from tkinter import *
from settings import *
from griddraw_discrete import *

pts=[]

def push_pts(event):
    pts.append((event.x, event.y))
    #print(pts)

def pop_pts(event):
    try:
        pts.pop()
    except IndexError:
        pass
    #print(pts)

def draw_cLine(event):
    canvas.delete('cLine')
    if is_near_snap(event):
        canvas.create_polygon(pts, outline=cLine_stroke, fill='#ccc', width=cLine_width, tag='cLine')
    else:
        canvas.create_line(pts, fill=cLine_stroke, width=cLine_width, tag='cLine')
        

def is_near_snap(event):
    try:
        target_x, target_y = pts[0][0], pts[0][1]
        min_x, max_x=target_x-snap_range, target_x+snap_range
        min_y, max_y=target_y-snap_range, target_y+snap_range
        if (event.x >= min_x and event.x <= max_x) and (event.y >= min_y and event.y <= max_y):
            return True
        else:
            return False
    except:
        return False

window=Tk()
canvas=Canvas(window, 
              width=window_width,
              height=window_height,
              background=window_bg)
canvas.grid(row=0, column=0, padx=padding, pady=padding)


canvas.bind('<Button-1>', push_pts)
canvas.bind('<Button-1>', draw_cLine, add='+')

canvas.bind('<Button-3>', pop_pts)
canvas.bind('<Button-3>', draw_cLine, add='+')



window.mainloop()