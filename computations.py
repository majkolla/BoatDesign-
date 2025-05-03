import numpy as np
from scipy.integrate import dblquad

def volume_for_lift(): 
    h = 1.0

    y_clip = 0.7

    def x_min():
        return -np.sqrt(1 - y_clip**2)

    def x_max():
        return np.sqrt(1 - y_clip**2)

    def y_lower(x):
        return -np.sqrt(1 - x**2)

    def y_upper(x):
        return min(y_clip, np.sqrt(1 - x**2))   

    area, error = dblquad(lambda y, x: 1, x_min(), x_max(), y_lower, y_upper)

    volume = h * area

    print(f"This is the volume: {volume}")

def volume_for_weight(): 
    pass


