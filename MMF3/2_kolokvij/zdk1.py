import math
import numpy as np
import matplotlib.pyplot as plt


# sve valja

a = 2
b = 1

v1 = -0.2
v2 = 3

def f(v):
    y = a*math.exp(v) + b*v**5
    return y



def gauge(x1, x2, n):
    x = []
    w = []
    EPS = 0.000001
    
    for k in range(0, n+1):
        x.append(k)
        w.append(k)

    m = int((n+1)/2)
    xm = 0.5*(x2 + x1)
    xl = 0.5*(x2 - x1)

    for i in range(1, m+1):
        z=math.cos(math.pi*(i - 0.25)/(n + 0.5))  # određuje nultočke

        while True:
            p1 = 1
            p2 = 0

            for j in range(1, n+1):
                p3 = p2
                p2 = p1
                p1 = ((2*j - 1)*z*p2-(j - 1)*p3)/j

            pp = n*(z*p1 - p2)/(z*z - 1)
            z1 = z
            z = z1 - p1/pp

            if (abs(z-z1) < EPS):      # do while ima obrnuto značenje od if
                break

        x[i] = xm - xl*z
        x[n+1-i] = xm + xl*z

        w[i] = 2*xl/((1-z*z)*pp*pp)
        w[n+1-i] = w[i]

        I = 0

        for i in range(1, len(x)):
            I = I + f(x[i])*w[i]

    return I, n



print('GauLeg',  gauge(v1, v2, 5)[1], ':', gauge(v1, v2, 5)[0])