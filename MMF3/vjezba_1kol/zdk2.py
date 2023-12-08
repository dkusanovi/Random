import numpy as np
import math
import matplotlib.pyplot as plt

epsilon = 10**(-5)


x = np.arange(-5, 91, 0.01)
u, d, s = [], [], []
for i in x:
    u.append(9*i**4-8*i**2-i-6+10*math.cos(2*i))
for ii in x:
    d.append(-(36*ii**3-16*ii-1-10*math.sin(2*ii)*2))
for iii in x:
    s.append(-(36*3*iii**2-16-40*math.cos(2*iii)))

def U(x):
    return 9*x**4-8*x**2-x-6+10*math.cos(2*x)

def derivative(x):
    return -(36*x**3-16*x-1-20*math.sin(2*x))


def bisekcija(a, b):
    n = 0
    while (abs(b-a) >= epsilon):
        n = n+1
        c = (a+b)/2
        f_a = derivative(a)
        f_c = derivative(c)
        if (f_a*f_c) < 0:
            a = a
            b = c
        elif (f_a*f_c) > 0:
            b = b
            a = c
        elif (n == 100):
            break
    print(n)
    return c
        


nn = bisekcija(-0.5, 0.5)

if derivative(nn) < 0:
    print('minimum:', nn)
elif derivative(nn) > 0:
    print('maksimum:', nn)
else:
    print('potrebno je provoditi daljnja testiranja')

fig, ax = plt.subplots()
ax.grid()
ax.set(xlabel='', ylabel='')
ax.plot(x, u, label='potencijal')
ax.plot(x, d, label='derivacija')
ax.plot(x, s, label='druga derivacija')
plt.legend(loc="upper left")
ax.set_xlim([-2, 2])
ax.set_ylim([-30, 50])

plt.show()