import math
import numpy as np
import matplotlib.pyplot as plt
import vjezbe7


t0 = 0
tN = 20
N = 20000
l = 0.2484902028828339
m = 0.2
g = 9.81
pi = 3.141592653589793


def JUG(y0, yd0):  # jednoliko ubrzano gibanje
    tlist = [t0]
    yd = [yd0]
    ydd = [-(g/l)*math.sin(y0*pi/180)]
    y = [y0/180*pi]
    h=(tN-t0)/N

    for i in range(0, N):
        tlist.append(i*h)
        y.append(y[i] + yd[-1]*h + 1/2*ydd[i-1]*h**2)
        yd.append(yd[i] + ydd[i]*h)
        ydd.append(-(g/l)*math.sin(y[i]))

    return tlist, y, yd, ydd



te, ipsilon, ipsilonder, ipsilonderder = JUG(4, 0)
e1, e2, e3, e4 = vjezbe7.euler(0, 4, 20000, 20)
RK41, RK42, RK43 = vjezbe7.RK4(0, 4, 20000, 20)

plt.plot(ipsilon[17000:20000], ipsilonder[17000:20000], color="b")
plt.plot(e2[17000:20000], e3[17000:20000], color="g")
plt.plot(RK42[17000:20000], RK43[17000:20000], color="r")

plt.legend(["JUG","Euler","RK4"])
plt.xlabel('kut [rad]')
plt.ylabel('kutna brzina [rad/$s$]')

plt.show()