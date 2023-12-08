import numpy as np
import math
import matplotlib.pyplot as plt
from polint import polint
from scipy.interpolate import CubicSpline


a =  0.52917721092
hartee = 315775.04
stupac1, stupac2 = [], []

with open('V(H-H).txt', 'r') as f:
    for line in f:
        if line.startswith('#'):
            continue
        else:
            lista = line.split(' ')
            stupac1.append(float(lista[0])*a)
            stupac2.append(float(lista[3])*hartee)



with open('V(H-H)_AK.txt', 'w') as f:
    f.writelines("%20s %20s " %('r_i', 'V_i'))

    f.write('\n')

    for i in range(0, len(stupac1)):
        f.writelines("\n%+20.6e %+20.9e" %(stupac1[i], stupac2[i]))

    f.close()




def lagrange(listX, listY, x, m):
    P = 0
    for i in range(m+1):
        L = 1
        for j in range(m+1):
            if j != i:
                L = L*(x-listX[j])/(listX[i]-listX[j])
        P = P + listY[i]*L
    return P

lag, listk, y_neville, greska_neville = [], [], [], []

for brojac in np.linspace(2.81, 9.82, 71):
    lag.append(lagrange(stupac1, stupac2, brojac, 38))
    listk.append(brojac)

    yn, dy = polint(stupac1, stupac2, len(stupac1)-1, brojac)
    y_neville.append(yn)
    greska_neville.append(dy)


def der(r):
    return -6*r**(-7)*(-45064)

der0 = (stupac2[1]-stupac2[0])/(stupac1[1]-stupac1[0])


cs = CubicSpline(stupac1, stupac2, bc_type=((1, der0), (1, der(stupac1[-1]))))
xs = np.linspace(2.81, 9.82, 71)




fig, ax = plt.subplots()
ax.grid()
ax.set(xlabel='$r / A$', ylabel='$V / K$')
ax.plot(listk, lag, 'ro', label='Lagrange')
ax.scatter(stupac1, stupac2, label='$(r_i, V_i)$', facecolors='none', edgecolors='k')
ax.errorbar(listk, y_neville, yerr=greska_neville, label='Neville', fmt='.')
ax.scatter(listk, cs(xs), label='CubicSpline', color='y')
plt.legend(loc="upper left")
ax.set_xlim([0, 10])
ax.set_ylim([-10, 10])

plt.show()


with open('V(H-H)_inter.txt', 'w') as f:
    f.writelines("%20s %20s %20s %20s %20s %20s " %('r', 'Lagrange', 'Neville', 'Neville greska', 'Spline', 'Neville - Spline'))

    f.write('\n')

    for i in range(0, len(listk)):
        f.writelines("\n%+20.6e %+20.6e %+20.6e %+20.6e %+20.6e %+20.6e" %(listk[i], lag[i], y_neville[i], greska_neville[i], cs(xs)[i], y_neville[i]-cs(xs)[i]))

    f.close()