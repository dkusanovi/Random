import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(x):
    return 1/math.sqrt(1-x)

listX = [-5, -4.7, -1.25, -0.01]
listY = []


for i in listX:
    ys = f(i)
    listY.append(ys)
print(listY)


def der(x):
    return -1/2*(1-x)**(-3/2)*(-1)

der0 = (listY[1]-listY[0])/(listX[1]-listX[0])


cs = CubicSpline(listX, listY, bc_type=((1, der0), (1, der(listX[-1]))))
xs = np.arange(-5, 0, 0.5)

fig, ax = plt.subplots()
ax.grid()
ax.set(xlabel='$r / A$', ylabel='$V / K$')
ax.scatter(listX, listY, label='tocke')
ax.scatter(xs, cs(xs), label='CubicSpline', color='y')
plt.legend(loc="upper left")
# ax.set_xlim([-100, 500])
# ax.set_ylim([-0.2, 1.6])

plt.show()