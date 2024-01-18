import math
import numpy as np
import matplotlib.pyplot as plt

# valja

m = 3.37*10**(-26)
T = 300
k = 1.38064852*10**(-23)
v1 = 0
v2 = 559.4

def f(v):
    y = (m/(2*math.pi*k*T))**(3/2)*4*math.pi*v**2*math.exp(-(m*v**2)/(2*k*T))
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
        z=math.cos(math.pi*(i - 0.25)/(n + 0.5))

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


print('GauLeg za',  gauge(v1, v2, 10)[1], 'tocaka:', gauge(v1, v2, 10)[0])
print('GauLeg za',  gauge(v1, v2, 50)[1], 'tocaka:', gauge(v1, v2, 50)[0])
print('GauLeg za',  gauge(v1, v2, 100)[1], 'tocaka:', gauge(v1, v2, 100)[0])