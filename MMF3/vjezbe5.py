import numpy as np
import math
import matplotlib.pyplot as plt


listX = [1, 2, 3, 4, 5]
listY = []

def y_function():
    for t in range (1, len(listX)+1):
        y = -2*t-4*t**2+t**3
        listY.append(y)
    return listY

y_function()


def function(listX, listY, x, m):
    P = 0
    for i in range(m+1):
        L = 1
        for j in range(m+1):
            if j != i:
                L = L*(x-listX[j])/(listX[i]-listX[j])
        P = P + listY[i]*L
    return P

second, third, listk = [], [], []

for k in range(0, 6000):
    brojac = k/1000
    second.append(function(listX, listY, brojac, 2))
    third.append(function(listX, listY, brojac, 3))
    listk.append(brojac)

fig, ax = plt.subplots()
ax.grid()
ax.set(xlabel='$t$', ylabel='$x$')
ax.plot(listk, second, label='$P_2(t)$')
ax.plot(listk, third, label='$P_3(t)$')
ax.plot(listX, listY, 'bo', label='$X_4$')
plt.legend(loc="upper left")
ax.set_xlim([0, 6])
ax.set_ylim([-20, 20])

plt.show()
