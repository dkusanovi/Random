import math
import numpy as np
import matplotlib.pyplot as plt


m = 3.37*10**(-26)
T = 300
k = 1.38064852*10**(-23)

x = np.arange(-5, 4000, 0.1)
funkcija, derivacija = [], []
for i in x:
    funkcija.append((m/(2*math.pi*k*T))**(3/2)*4*(math.pi)*(i**2)*(math.exp(-(m*i**2)/(2*k*T)))-1.3*10**(-3))

for i in x:
    derivacija.append((m/(2*math.pi*k*T))**(3/2)*4*math.pi*math.exp(-m*i**2/(2*k*T))*(2*i-i**3*m/(k*T)))


def f(v):
    y = (m/(2*math.pi*k*T))**(3/2)*4*math.pi*v**2*math.exp(-(m*v**2)/(2*k*T)-1.3*10**(-3))
    return y

def derivative(v):
    y_der = (m/(2*math.pi*k*T))**(3/2)*4*math.pi*math.exp(-m*v**2/(2*k*T))*(2*v-v**3*m/(k*T))
    return y_der


for ii in np.linspace(0, 1000):
    s = (m/(2*math.pi*k*T))**(3/2)*4*(math.pi)*(ii**2)*(math.exp(-(m*ii**2)/(2*k*T)))-1.3*10**(-3)
    if abs(s) < 10**(-8):
        print(ii)

    

epsilon = 10**(-8)

def bisekcija(a, b):
    n = 0
    while (abs(b-a) >= epsilon):
        n = n + 1
        c = (a+b)/2
        f_a = f(a)
        f_c = f(c)
        if (f_a*f_c) < 0:
            a = a
            b = c
        elif (f_a*f_c) > 0:
            b = b
            a = c
        elif (n == 100):
            break
    print(n)
    print(c)


def newton_raphson(x, n):
    i = 0
    while (abs(f(x)/(derivative(x)))) >= epsilon:
        n = n + 1
        i = i + 1
        x = x - f(x)/derivative(x)
        if derivative(x) == 0:
            break
        elif (i == 500):
            break
    print(i)
    print(x)



bisekcija(331, 331.5)
newton_raphson(200, 1)

fig, ax = plt.subplots()
ax.grid()
ax.set(xlabel='', ylabel='')
ax.plot(x, funkcija, label='funkcija')
ax.plot(x, derivacija, label='derivacija')
plt.legend(loc="upper right")
# ax.set_xlim([-100, 100])
# ax.set_ylim([-2, 0])

plt.show()