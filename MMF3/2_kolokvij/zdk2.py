import math
import numpy as np
import matplotlib.pyplot as plt


# kod izgleda dobro, ali graf malo prebrzo propagira

t0 = 0
tN = 2
N = 2000
g = 9.81
# q0 = 0
C = 500*10**(-6)

omega = 2*math.pi

def JUG(y0, yd0):  # jednoliko ubrzano gibanje
    tlist = [t0]
    yd = [yd0]
    ydd = [-5*(omega)**2*math.sin(omega*t0)*C]
    y = [y0]
    h = (tN-t0)/N

    for i in range(0, N):
        tlist.append(h+i*h)
        y.append(y[i] + yd[-1]*h + 1/2*ydd[i-1]*h**2)
        yd.append(yd[i] + ydd[i]*h)
        ydd.append(-5*C*(omega)**2*math.sin(tlist[i]*omega))

    return tlist, y, yd, ydd



te, ipsilon, ipsilonder, ipsilonderder = JUG(0, 5*C*omega*math.cos(omega*t0))
plt.grid()
plt.plot(te, ipsilon, color="b")

# plt.xlim([0, 0.8])
plt.legend(["JUG"])
plt.xlabel('t')
plt.ylabel('q')

plt.show()