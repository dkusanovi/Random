import numpy as np
import math
import matplotlib.pyplot as plt



def prvi_a(x, n):

    H0 = 1
    H1 = 2*x
    H_list = []

    k = 2
    for k in range(1,n,1):
        h =  2*x*H1 - 2*(k)*H0
        H0 = H1
        H1 = h
        H_list.append(h)

    return h

prvi_a(10, 10)



hlist = [10**(-1), 10**(-3)]



def unaprijed(x, h):
    u = (prvi_a(x+h, 10)-prvi_a(x, 10))/h
    return u

def centralna(x, h):
    c = (prvi_a(x+h, 10)-prvi_a(x-h, 10))/(2*h)
    return c

print('unaprijed h=10**(-1):', unaprijed(10, hlist[0]))
print('unaprijed h=10**(-3):', centralna(10, hlist[0]))
print('unaprijed h=10**(-1):', unaprijed(10, hlist[1]))
print('unaprijed h=10**(-3):', centralna(10, hlist[1]))