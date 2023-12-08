import numpy as np
import math
import matplotlib.pyplot as plt



# epsilon = 10**(-10) # NIJE JEDNAKO epsilon = 10^(-10)


## a) preko reda e^(-x)

def a(x):

    epsilon = 10**(-10)


    s0 = 1
    sa = s0
    k = 0
    while abs(s0) >= epsilon:
        k = k + 1
        s0 = (((-1)**k)*(x**k))/math.factorial(k)
        sa = sa + s0

    return k, sa


## b)  rekurzivnom formulom

def b(x):

    epsilon = 10**(-10)


    clan = 1
    sb = clan
    k = 0
    while abs(clan) >= epsilon: 
        k = k + 1
        clan = -clan*(x/k)
        sb = sb + clan

    return k, sb



## c) izracunati e^x i onda 1/e^x

def c_python(x):
    e = math.exp(x)
    jedan_kroz_enaminusiks = 1/e

    return jedan_kroz_enaminusiks


def c(x):

    epsilon = 10**(-10)

    s0 = 1
    sc = s0
    k = 0
    while abs(s0) >= epsilon:
        k = k + 1
        s0 = ((x**k))/math.factorial(k)
        sc = sc + s0

    jedan_kroz_enaminusiks1 = 1/sc


    return jedan_kroz_enaminusiks1






with open('vjezba1_table.txt', 'w') as f:
    f.writelines("%20s %20s %20s %20s %20s %20s" %("x", "broj iteracija", "red a)", "rekurzija b)", "1\\red c)", "e^(-x) python"))

    f.write('\n')

    for i in range(0, 11):
        i *= 10
        f.writelines("\n%+20d %+20d %+20.6e %+20.6e %+20.6e %+20.6e" %(i, a(i)[0], a(i)[1], b(i)[1], c(i), c_python(i)))


    f.close()