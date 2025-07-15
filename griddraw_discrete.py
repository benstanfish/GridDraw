__version__ = '1.0'

# from tkinter import *
# from settings import *

def get_axis_points(min, max, units):
    length=max-min
    points=[i for i in range(length+1) if i % units == 0]
    centroid=(length-points[-1])/2+min
    corrected_points=[i+centroid for i in points]
    return corrected_points

def draw_point(event):
    cx = event.x
    cy = event.y
    canvas.create_oval(cx-radius,
                       cy-radius,
                       cx+radius,
                       cy+radius,
                       outline=oval_stroke,
                       fill=oval_fill,
                       width=oval_stroke_width)

def draw_line(event):
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
                           fill=line_fill,
                           width=line_width)
        click_number=0

xs=get_axis_points(min=grid_x_min, max=grid_x_max, units=grid_unit)
ys=get_axis_points(min=grid_y_min, max=grid_y_max, units=grid_unit)

window=Tk()
window.title('Draw on Grid v' + __version__)

canvas=Canvas(window, 
              width=window_width,
              height=window_height,
              background=window_bg)
canvas.grid(row=0, column=0, padx=padding, pady=padding)

for col in range(len(ys)-1):
    for row in range(len(xs)-1):
        canvas.create_rectangle(xs[row], ys[col], 
                                xs[row+1], ys[col+1],
                                outline=grid_color,
                                width=grid_weight,
                                fill=grid_fill)

# canvas.bind('<Button-1>', draw_point)
# canvas.bind('<Button-1>', draw_line, add='+')
# click_number=0

window.mainloop()