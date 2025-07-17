

def get_waypoints(min, max, units, shift=0):
    return [i+min+shift for i in range(max-min+1) if (i+min) % units == 0]