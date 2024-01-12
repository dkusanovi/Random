import math
import numpy as np
import matplotlib.pyplot as plt



Mlist = [0, 100, 200, 300, 400]

dx = 0.2
dt = 0.5
tlist = []

for jj in Mlist:
    tlist.append(dt*jj)



# poc_uvjeti= [t0, tN, x0, xN, dx, dt]
poc_uvjeti1 = [0, tlist[0], 0, 20, dx, dt]
poc_uvjeti2 = [0, tlist[1], 0, 20, dx, dt]
poc_uvjeti3 = [0, tlist[2], 0, 20, dx, dt]
poc_uvjeti4 = [0, tlist[3], 0, 20, dx, dt]
poc_uvjeti5 = [0, tlist[4], 0, 20, dx, dt]


def gx(x):
    if x<5 and x>2:
        return 5.5
    else:
        return 0.0



def eksplicitno(gx, poc_uvjeti, D):
    dx = poc_uvjeti[4]
    dt = poc_uvjeti[5]
    alpha = D*dt/dx**2

    N = int((poc_uvjeti[3]-poc_uvjeti[2])/dx)
    M = int((poc_uvjeti[1]-poc_uvjeti[0])/dt)

    rub_l = 0.0
    rub_d = 0.0

    prva = np.zeros(N+1) # upoc
    druga = np.zeros(N+1) # u novo

    for i in range(len(prva)):
        prva[i] = gx(poc_uvjeti[2]+i*dx)

    for j in range(M+1):

        for ii in range(1, N):
            druga[ii] = alpha*prva[ii+1]+(1-2*alpha)*prva[ii]+alpha*prva[ii-1]

        druga[0] = rub_l
        druga[-1] = rub_d

        prva = np.copy(druga)

    return druga

jedan = eksplicitno(gx, poc_uvjeti1, 10**(-2))
dva = eksplicitno(gx, poc_uvjeti2, 10**(-2))
tri = eksplicitno(gx, poc_uvjeti3, 10**(-2))
cetiri = eksplicitno(gx, poc_uvjeti4, 10**(-2))
pet = eksplicitno(gx, poc_uvjeti5, 10**(-2))

xlist = []

for k in np.arange(0.0, 20+dx, dx):
    xlist.append(k/dx)

fig, ax = plt.subplots()
ax.grid()
plt.plot(xlist, jedan)
plt.plot(xlist, dva)
plt.plot(xlist, tri)
plt.plot(xlist, cetiri)
plt.plot(xlist, pet)
plt.legend(['0', '100', '200', '300', '400'])

plt.show()



def matrica(a, b, c, d):
    n = len(d) - 1

    ccc = [c[0]/b[0]]
    dcc = [d[0]/b[0]]
    

    for i in range (1, n):
        ccc.append((c[i])/(b[i]-a[i]*ccc[i-1]))
        dcc.append((d[i]-a[i]*dcc[i-1])/(b[i]-a[i]*ccc[i-1]))

    dcc.append((d[n]-a[n]*dcc[n-1])/(b[n]-a[n]*ccc[n-1]))

    x = [dcc[n]]

    for j in range(1, n+1):
        k = n - j
        x.append(dcc[k]-ccc[k]*x[j-1])
    x.reverse()

    return x



def implicitno(gx, poc_uvjeti, D):
    dx = poc_uvjeti[4]
    dt = poc_uvjeti[5]
    alpha = D*dt/dx**2

    N = int((poc_uvjeti[3]-poc_uvjeti[2])/dx)
    M = int((poc_uvjeti[1]-poc_uvjeti[0])/dt)

    rub_l = 0.0
    rub_d = 0.0

    prva = np.zeros(N+1) # u poc
    druga = np.zeros(N+1) # u novo

    for i in range(len(prva)):
        prva[i] = gx(poc_uvjeti[2]+i*dx)
    
    
    a = [-alpha]*N
    b = [1+2*alpha]*(N+1)
    c = [-alpha]*N
    a.insert(0, 0)
    c.append(0)


    for j in range(M+1):
        druga = matrica(a, b, c, prva)

        druga[0] = rub_l
        druga[-1] = rub_d

        prva = np.copy(druga)


    return druga


jedan = implicitno(gx, poc_uvjeti1, 10**(-2))
dva = implicitno(gx, poc_uvjeti2, 10**(-2))
tri = implicitno(gx, poc_uvjeti3, 10**(-2))
cetiri = implicitno(gx, poc_uvjeti4, 10**(-2))
pet = implicitno(gx, poc_uvjeti5, 10**(-2))

xlista = []

for k in np.arange(0.0, 20+dx, dx):
    xlista.append(k/dx)

fig, ax = plt.subplots()
ax.grid()
plt.plot(xlista, jedan)
plt.plot(xlista, dva)
plt.plot(xlista, tri)
plt.plot(xlista, cetiri)
plt.plot(xlista, pet)
plt.legend(['0', '100', '200', '300', '400'])

plt.show()







