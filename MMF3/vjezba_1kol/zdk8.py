import math
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-5, 91, 0.01)
funkcija, derivacija = [], []
for i in x:
    funkcija.append(math.sin(2*i)-2*math.cos(i))

for i in x:
    derivacija.append(2*math.cos(2*i)+ 2*math.sin(i))

def f(x):
    y = math.sin(2*x)-2*math.cos(x)
    return y

def derivative(x):
    y_der = 2*math.cos(2*x)+ 2*math.sin(x)
    return y_der

epsilon = 10**(-6)

def bisekcija(a, b):

    while abs(b-a) >= epsilon:
        c = (a+b)/2
        f_a = f(a)
        f_c = f(c)
        if (f_a*f_c) < 0:
            a = a
            b = c
        elif (f_a*f_c) > 0:
            b = b
            a = c
    print(c)


def newton_raphson(x, n):
    while (abs(f(x)/(derivative(x)))) >= epsilon:
        n = n + 1
        x = x - f(x)/derivative(x)
        if derivative(x) == 0:
            break
    print(x)


bisekcija(0, 2)
newton_raphson(0.5, 1)

fig, ax = plt.subplots()
ax.grid()
ax.set(xlabel='', ylabel='')
ax.plot(x, funkcija, label='funkcija')
ax.plot(x, derivacija, label='derivacija')
plt.legend(loc="upper left")
ax.set_xlim([-2, 2])
ax.set_ylim([-10, 10])

plt.show()