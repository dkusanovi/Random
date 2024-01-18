import math
import numpy as np
import matplotlib.pyplot as plt


# grafički problem za t=0, 6 i 8 dobri


dx = 0.1
dt = 0.005
tlist = [0, 6*dt, 8*dt]



# poc_uvjeti= [t0, tN, x0, xN, dx, dt]
poc_uvjeti0 = [0, dt, 0, 1, dx, dt]
poc_uvjeti1 = [0, tlist[0], 0, 1, dx, dt]
poc_uvjeti2 = [0, tlist[1], 0, 1, dx, dt]
poc_uvjeti3 = [0, tlist[2], 0, 1, dx, dt]


def gx(x):
    if x>=0 and x<=(1/5):
        return -x
    elif x>(1/5) and x<=(8/10):
        return x-2/5
    elif x>(8/10) and x<=1:
        return 1-x 
    # else:
    #     return 0.0



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

print('rješenja eksplicitno:', eksplicitno(gx, poc_uvjeti1, 1))

jedan = eksplicitno(gx, poc_uvjeti1, 1)
dva = eksplicitno(gx, poc_uvjeti2, 1)
tri = eksplicitno(gx, poc_uvjeti3, 1)

xlist = []

for k in np.arange(0.0, 1+dx, dx):
    xlist.append(k/dx)

fig, ax = plt.subplots()
ax.grid()
ax.set_title('eksplicitno')
plt.plot(xlist, jedan)
plt.plot(xlist, dva)
plt.plot(xlist, tri)
plt.xlabel('$x$')
plt.ylabel('$u$')
# plt.plot(xlist, cetiri)
# plt.plot(xlist, pet)
plt.legend(['0', '6*dt', '8*dt'])

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


print('rješenja implicitno:', implicitno(gx, poc_uvjeti1, 1))

jedan = implicitno(gx, poc_uvjeti1, 1)
dva = implicitno(gx, poc_uvjeti2, 1)
tri = implicitno(gx, poc_uvjeti3, 1)

xlista = []

for k in np.arange(0.0, 1+dx, dx):
    xlista.append(k/dx)

fig, ax = plt.subplots()
ax.grid()
ax.set_title('implicitno')
plt.plot(xlista, jedan)
plt.plot(xlista, dva)
plt.plot(xlista, tri)
plt.xlabel('$x$')
plt.ylabel('$u$')
# plt.plot(xlista, cetiri)
# plt.plot(xlista, pet)
plt.legend(['0', '6*dt', '8*dt'])

plt.show()







