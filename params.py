from user_settings import *

# selected_theme='default'
graph_themes = {
    'green': {
        'background':'#f6fbc0',
        'minor': '#83e6a2',
        'major': '#3e8052'
    },
    'blue': {
        'background':"#3969e4",
        'minor': "#949FBB",
        'major': "#fefeff"
    },
    'light': {
        'background':'#ffffff',
        'minor': '#cccccc',
        'major': '#555555'
    },
    'dark': {
        'background':'#555555',
        'minor': '#999999',
        'major': '#cccccc'
    },
    'default': {
        'background':'#ffffff',
        'minor': '#cccccc',
        'major': '#555555'
    }
}
theme={
    'background':graph_themes[selected_theme]['background'],
    'minor': graph_themes[selected_theme]['minor'],
    'major': graph_themes[selected_theme]['major']
}

window_params = {
    'width': 800,
    'height': 600,
    'fill': theme['background'],
    'padding': 5
}

i_minor = {
    'space': 20,
    'color': theme['minor'],
    'width': 1,
    'shift': 5
}

i_major = {
    'space': i_minor['space']*5,
    'color':theme['major'],
    'width': 1,
    'shift': 5
}

j_minor = {
    'space': i_minor['space'],
    'color': i_minor['color'],
    'width': i_minor['width'],
    'shift': i_minor['shift']
}

j_major = {
    'space': i_major['space'],
    'color': i_major['color'],
    'width': i_major['width'],
    'shift': i_major['shift']
}

node_oval = {
    'radius': 1,
    'outline': '#000000',
    'fill': '#000000',
    'width': 4
}   