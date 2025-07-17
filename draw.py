__version__ = '1.0'

from tkinter import *
from params import *
from funcs import *
from draw_shapes import draw_line, draw_point

x_min=get_waypoints(min=0, max=window_params['width']-1, units=i_minor['space'], shift=i_minor['shift'])
x_maj=get_waypoints(min=0, max=window_params['width']-1, units=i_major['space'], shift=i_major['shift'])
y_min=get_waypoints(min=0, max=window_params['height']-1, units=j_minor['space'], shift=j_minor['shift'])
y_maj=get_waypoints(min=0, max=window_params['height']-1, units=j_major['space'], shift=j_major['shift'])

window=Tk()
window.title('Draw on Grid v' + __version__)

canvas=Canvas(window, 
              width=window_params['width'],
              height=window_params['height'],
              background=window_params['fill'])

canvas.grid(row=1, column=1, 
            padx=window_params['padding'], 
            pady=window_params['padding'])

for vert in range(len(x_min)):
    canvas.create_line((x_min[vert], 0, 
                        x_min[vert], window_params['height']), 
                        fill=i_minor['color'],
                        width=i_minor['width'])

for horiz in range(len(y_min)):
    canvas.create_line((0, y_min[horiz],
                        window_params['width'], y_min[horiz]), 
                        fill=j_minor['color'],
                        width=j_minor['width'])

for vert in range(len(x_maj)):
    canvas.create_line((x_maj[vert], 0, 
                        x_maj[vert], window_params['height']), 
                        fill=i_major['color'],
                        width=i_major['width'])

for horiz in range(len(y_maj)):
    canvas.create_line((0, y_maj[horiz],
                        window_params['width'], y_maj[horiz]), 
                        fill=j_major['color'],
                        width=j_major['width'])


canvas.bind('<Button-1>', lambda event: draw_point(event, canvas=canvas))
canvas.bind('<Button-1>', lambda event: draw_line(event, canvas=canvas), add='+')
click_number=0

window.mainloop()