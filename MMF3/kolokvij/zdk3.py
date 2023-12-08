import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from polint import polint


def f(x):
    return (x-5)*(x-4)*(x-3)*(x-2)*(x-1)*x

listX = []
listY = []

for i in np.arange(0, 3, 0.2307692308):
    # iks = f(i)
    listX.append(i)


for i in listX:
    ys = f(i)
    listY.append(ys)

print(listX)
print(listY)

h = 10**(-5)

def der(xs):
    derivacija = (f(xs+h)-f(xs-h))/(2*h)
    return derivacija


y_neville, greska_neville = [], []

for brojac in np.linspace(0, 3, 81):

    yn, dy = polint(listX, listY, len(listX)-1, brojac)
    y_neville.append(yn)
    greska_neville.append(dy)

der0 = (listY[1]-listY[0])/(listX[1]-listX[0])


cs = CubicSpline(listX, listY, bc_type='natural')
xss = np.linspace(0, 3, 81)

fig, ax = plt.subplots()
ax.grid()
ax.set(xlabel='', ylabel='')
ax.scatter(listX, listY, color='red', label='tocke')
ax.scatter(xss, cs(xss), label='CubicSpline', color='y')
ax.errorbar(xss, y_neville, yerr=greska_neville, label='Neville', fmt='.')
plt.legend(loc="upper left")
# ax.set_xlim([-100, 500])
# ax.set_ylim([-0.2, 1.6])

plt.show()