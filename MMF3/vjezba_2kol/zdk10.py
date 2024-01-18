import math
import numpy as np
import matplotlib.pyplot as plt

# valja ali fali sila na grafu

m = 2
g = 9.81

def ydd(y, yd,  t0):     # funkcija akceleracije
    return (2*y - 5*yd + 0.5)/m

def RK4(t0, y0, N, N_perioda):
    y = [y0/180*math.pi]
    yd = [0]
    t = [t0]
    tN = 5
    # tN = N_perioda*2*math.pi*math.sqrt(2/m)  # vrijeme n-te tocke
    dt = (tN-t0)/N


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

    return t, y, yd




def prvih_pet():
    fig, ax = plt.subplots()
    ax.grid()
    plt.plot(RK4(0, 0, 10000, 5)[0],  RK4(0, 0, 10000, 5)[1], label='10000')
    plt.plot(RK4(0, 0, 20000, 5)[0],  RK4(0, 0, 20000, 5)[1], label='20000')
    # plt.plot(RK4(0, 0, 40000, 20)[0],  RK4(0, 0, 40000, 20)[1], label='40000')
    # plt.plot(RK4(0, 0, 80000, 20)[0],  RK4(0, 0, 80000, 20)[1], label='80000')
    # plt.plot(RK4(0, 0, 160000, 20)[0],  RK4(0, 0, 160000, 20)[1], label='160000')
    # plt.plot(RK4(0, 0, 320000, 20)[0],  RK4(0, 0, 320000, 20)[1], label='320000')
    # plt.plot(RK4(0, 0, 640000, 20)[0],  RK4(0, 0, 640000, 20)[1], label='640000')
    # ax.set_xlim([0, 5])
    # ax.set_ylim([0, 1])
    ax.set(xlabel='$t$', ylabel='$y$')
    plt.legend(loc="upper left")
    plt.show()

# prvih_pet()

def graf2():
    fig, ax = plt.subplots()
    ax.grid()
    plt.plot(RK4(0, 0, 10000, 5)[0], RK4(0, 0, 10000, 5)[1] , label='polozaj')
    plt.plot(RK4(0, 0, 10000, 5)[0],  RK4(0, 0, 10000, 5)[2], label='brzina')
    #plt.plot(RK4(0, 0, 10000, 5)[0],  , label='sila')
    #ax.set(xlabel='$t$', ylabel='$y$')
    plt.legend(loc="upper left")
    plt.show()

graf2()
