import math
import numpy as np
import matplotlib.pyplot as plt


# valja napisano, fali d)

m = 20/1000
g = 9.81
pi = 3.141592653589793
k = 80/1000
b = 4/1000

def analiticki(y0, t):
    return y0*math.exp(-b*t/(2*m))*math.cos((math.sqrt(k/m-b**2/(4*m**2)))*t)

def ydd(y, yd,  t0):     # funkcija akceleracije
    return (-k*y-b*yd)/m



def RK4(t0, y0, N, N_perioda):
    y = [y0/180*pi]
    yd = [0]
    t = [t0]
    # tN = 20
    tN = N_perioda*2*pi*math.sqrt(k/m-b**2/(4*m**2))
    dt = (tN-t0)/N
    ya = [analiticki(y[0], 0)]


    while (len(yd) <= N):
        Y = y[-1]
        Yd = yd[-1]
        T = t[-1]

        k1x = Yd
        k1vx = ydd(Y, Yd, T) # nagib brzine

        k2x = Yd + k1vx*dt/2
        k2vx =  ydd(Y + k1x*dt/2, Yd + k1vx*dt/2, T + dt/2)

        k3x = Yd + k2vx*dt/2
        k3vx = ydd(Y + k2x*dt/2, Yd + k2vx*dt/2, T + dt/2)

        k4x = Yd + k3vx*dt
        k4vx = ydd(Y + k3x*dt, Yd + k3vx*dt, T + dt)

        t.append(T+dt)
        y.append(Y + 1/6*(k1x + 2*k2x + 2*k3x + k4x)*dt)
        yd.append(Yd + 1/6*(k1vx + 2*k2vx + 2*k3vx + k4vx)*dt)
        ya.append(analiticki(y[0], T))

    return t, y, yd, ya


def dvadeset_period_RK4():
    fig, ax = plt.subplots()
    ax.grid()
    plt.plot(RK4(0, 5/100, 10000, 20)[0], RK4(0, 5/100, 10000, 20)[3], label='analiticki')
    plt.plot(RK4(0, 5/100, 10000, 20)[0],  RK4(0, 5/100, 10000, 20)[1], label='10000')
    # plt.plot(RK4(0, 5/100, 20000, 20)[0],  RK4(0, 5, 20000, 20)[1], label='20000')
    # plt.plot(RK4(0, 5/100, 40000, 20)[0],  RK4(0, 5, 40000, 20)[1], label='40000')
    # plt.plot(RK4(0, 5/100, 80000, 20)[0],  RK4(0, 5, 80000, 20)[1], label='80000')
    # plt.plot(RK4(0, 5/100, 160000, 20)[0],  RK4(0, 5, 160000, 20)[1], label='160000')
    # plt.plot(RK4(0, 5/100, 320000, 20)[0],  RK4(0, 5, 320000, 20)[1], label='320000')
    # plt.plot(RK4(0, 5/100, 640000, 20)[0],  RK4(0, 5, 640000, 20)[1], label='640000')
    ax.set_xlim([0, 20])
    # ax.set_ylim([-0.02, 0.02])
    plt.legend(loc="upper right")
    plt.show()

dvadeset_period_RK4()