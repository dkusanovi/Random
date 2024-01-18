import math
import numpy as np
import matplotlib.pyplot as plt

# valja

v1 = -0.5
v2 = 2


def f(v):
    y = math.exp(v) + v**5 
    return y



def trapez(lower, upper, mm):
    h = (upper-lower)/mm
    br = 0.5 * (f(lower) + f(upper))*h

    for i in range(1, mm):
        br = br + h*f(lower+i*h)
    return br

print('trapez 10 tocaka:', trapez(v1, v2, 10))
print('trapez 50 tocaka:', trapez(v1, v2, 50))
print('trapez 100 tocaka:', trapez(v1, v2, 100))




def simpson(lower, upper, mm):
    h = (upper-lower)/mm
    br = (f(lower) + f(upper))*h*1/3

    for i in range(1, mm):
        if (i % 2) == 0:
            br = br + 2*f(lower+i*h)*h/3
        else:
            br = br + 4*f(lower+i*h)*h/3

    return br

print('simpson 10 tocaka:', simpson(v1, v2, 10))
print('simpson 50 tocaka:', simpson(v1, v2, 50))
print('simpson 100 tocaka:', simpson(v1, v2, 100))