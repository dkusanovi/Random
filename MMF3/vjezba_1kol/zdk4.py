import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

H = [0, 50, 100, 150, 200, 250, 300]
B = [0, 0.2, 0.75, 1.2, 1.4, 1.48, 1.5]


def lagrange(listX, listY, x, m):
    P = 0
    for i in range(m+1):
        L = 1
        for j in range(m+1):
            if j != i:
                L = L*(x-listX[j])/(listX[i]-listX[j])
        P = P + listY[i]*L
    return P

lag, listk = [], []

for brojac in np.linspace(0, 300, 10):
    lag.append(lagrange(H, B, brojac, 6))
    listk.append(brojac)

xs = np.linspace(0, 300, 10)

cs = CubicSpline(H, B, bc_type='natural')

fig, ax = plt.subplots()
ax.grid()
ax.set(xlabel='$r / A$', ylabel='$V / K$')
ax.plot(listk, lag, 'ro', label='Lagrange')
ax.scatter(listk, cs(xs), label='CubicSpline', color='y')
plt.legend(loc="upper left")
ax.set_xlim([-100, 500])
ax.set_ylim([-0.2, 1.6])

plt.show()


with open('zdk4.txt', 'w') as f:
    f.writelines("%20s %20s %20s %20s " %('H [Am^(-1)]', 'B [T]', 'Lagrange', 'Spline'))

    f.write('\n')

    for i in range(0, len(H)):
        f.writelines("\n%+20.2d %+20.3e %+20.3e %+20.3e" %(H[i], B[i], lag[i], cs(xs)[i]))

    f.close()
