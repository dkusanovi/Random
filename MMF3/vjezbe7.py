import math
import numpy as np
import matplotlib.pyplot as plt



l = 0.2484902028828339
m = 0.2
g = 9.81
pi = 3.141592653589793


def analiticki(y0, t):
    return y0*math.cos(math.sqrt(g/l)*t)

def ydd(y, yd,  t0):     # funkcija akceleracije
    return -(g/l)*math.sin(y)

def euler(t0, y0, N, N_perioda):
    y = [y0/180*pi]
    yd = [0]
    t = [t0]
    ya = [analiticki(y[0], 0)]
    tN = N_perioda*2*pi*math.sqrt(l/g) # vrijeme n-te tocke
    h = (tN-t0)/N
    for i in range(0, N):
        t.append(t[0] + i*h)

        y.append(y[i] + yd[-1]*h)  #yd tiba bit zadnji clan a ne i-ti
        yd.append(yd[i] + ydd(y[i], y0, t0)*h)
        # kad su prethodne dvije linije obrnutim redoslijedom napisane, metoda ispada preciznija (mi trazimo manje preciznu)        

        ya.append(analiticki(y[0], t[i]))

    return t, y, yd, ya




def RK4(t0, y0, N, N_perioda):
    y = [y0/180*pi]
    yd = [0]
    t = [t0]
    tN = N_perioda*2*pi*math.sqrt(l/g)
    dt = (tN-t0)/N


    while (len(yd) <= N):
        Y = y[-1]
        Yd = yd[-1]
        T = t[-1]

        k1vx = ydd(Y, Yd, T)
        k1x = Yd

        k2vx =  ydd(Y + k1vx*dt/2, Yd + k1vx*dt/2, T + dt/2)
        k2x = Yd + k1vx*dt/2

        k3vx = ydd(Y + k2vx*dt/2, Yd + k2vx*dt/2, T + dt/2)
        k3x = Yd + k2vx*dt/2

        k4vx = ydd(Y + k3vx*dt, Yd + k3vx*dt, T + dt)
        k4x = Yd + k3vx*dt

        t.append(T+dt)
        y.append(Y + 1/6*(k1x + 2*k2x + 2*k3x + k4x)*dt)
        yd.append(Yd + 1/6*(k1vx + 2*k2vx + 2*k3vx + k4vx)*dt)

    return t, y, yd

# print(RK4(0, 4, 10000, 20)[0])
# print(RK4(0, 4, 10000, 20)[1])
# print(RK4(0, 4, 10000, 20)[2])








tlist2000, ylist2000, ydlist2000, yalist2000 = euler(0, 4, 2000, 20)
tlist20000, ylist20000, ydlist20000, yalist20000 = euler(0, 4, 20000, 20)
tlist200000, ylist200000, ydlist200000, yalist200000 = euler(0, 4, 200000, 20)


def jedan_period_euler():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4))
    ax[0].grid()
    ax[1].grid()
    ax[2].grid()
    ax[0].plot(tlist2000, ylist2000, 'r', label='Euler')
    ax[0].plot(tlist2000, yalist2000, 'b', label='Analiticki')
    ax[1].plot(tlist20000, ylist20000, 'r', label='Euler')
    ax[1].plot(tlist20000, yalist20000, 'b', label='Analiticki')
    ax[2].plot(tlist200000, ylist200000, 'r', label='Euler')
    ax[2].plot(tlist200000, yalist200000, 'b', label='Analiticki')
    ax[0].set_xlim([0, 1])
    ax[1].set_xlim([0, 1])
    ax[2].set_xlim([0, 1])
    # ax.set_ylim([0, 1])
    ax[0].legend(loc="lower left")
    ax[1].legend(loc="lower left")
    ax[2].legend(loc="lower left")
    ax[0].set_title('N=2000')
    ax[1].set_title('N=20000')
    ax[2].set_title('N=200000')
    plt.show()


def devetnaesti_period_euler():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4))
    ax[0].grid()
    ax[1].grid()
    ax[2].grid()
    ax[0].plot(tlist2000, ylist2000, 'r', label='Euler')
    ax[0].plot(tlist2000, yalist2000, 'b', label='Analiticki')
    ax[1].plot(tlist20000, ylist20000, 'r', label='Euler')
    ax[1].plot(tlist20000, yalist20000, 'b', label='Analiticki')
    ax[2].plot(tlist200000, ylist200000, 'r', label='Euler')
    ax[2].plot(tlist200000, yalist200000, 'b', label='Analiticki')
    ax[0].set_xlim([19, 20])
    ax[1].set_xlim([19, 20])
    ax[2].set_xlim([19, 20])
    # ax.set_ylim([0, 1])
    ax[0].legend(loc="lower left")
    ax[1].legend(loc="lower left")
    ax[2].legend(loc="lower left")
    ax[0].set_title('N=2000')
    ax[1].set_title('N=20000')
    ax[2].set_title('N=200000')
    plt.show()

# jedan_period_euler()
#devetnaesti_period_euler()








def jedan_period_RK4():
    fig, ax = plt.subplots()
    ax.grid()
    plt.plot(RK4(0, 4, 10000, 20)[0],  RK4(0, 4, 10000, 20)[1], label='10000')
    plt.plot(RK4(0, 4, 20000, 20)[0],  RK4(0, 4, 20000, 20)[1], label='20000')
    plt.plot(RK4(0, 4, 40000, 20)[0],  RK4(0, 4, 40000, 20)[1], label='40000')
    plt.plot(RK4(0, 4, 80000, 20)[0],  RK4(0, 4, 80000, 20)[1], label='80000')
    plt.plot(RK4(0, 4, 160000, 20)[0],  RK4(0, 4, 160000, 20)[1], label='160000')
    plt.plot(RK4(0, 4, 320000, 20)[0],  RK4(0, 4, 320000, 20)[1], label='320000')
    plt.plot(RK4(0, 4, 640000, 20)[0],  RK4(0, 4, 640000, 20)[1], label='640000')
    ax.set_xlim([0, 1])
    # ax.set_ylim([0, 1])
    plt.legend(loc="lower left")
    plt.show()

def devetnaesti_period_RK4():
    fig, ax = plt.subplots()
    ax.grid()
    plt.plot(RK4(0, 4, 10000, 20)[0],  RK4(0, 4, 10000, 20)[1], label='10000')
    plt.plot(RK4(0, 4, 20000, 20)[0],  RK4(0, 4, 20000, 20)[1], label='20000')
    plt.plot(RK4(0, 4, 40000, 20)[0],  RK4(0, 4, 40000, 20)[1], label='40000')
    plt.plot(RK4(0, 4, 80000, 20)[0],  RK4(0, 4, 80000, 20)[1], label='80000')
    plt.plot(RK4(0, 4, 160000, 20)[0],  RK4(0, 4, 160000, 20)[1], label='160000')
    plt.plot(RK4(0, 4, 320000, 20)[0],  RK4(0, 4, 320000, 20)[1], label='320000')
    plt.plot(RK4(0, 4, 640000, 20)[0],  RK4(0, 4, 640000, 20)[1], label='640000')
    ax.set_xlim([19, 20])
    # ax.set_ylim([0, 1])
    plt.legend(loc="lower left")
    plt.show()

# jedan_period_RK4()
# devetnaesti_period_RK4()             ovo je nepotrebno







listN = [10000, 20000, 40000, 80000, 160000, 320000, 640000]

def periodi_razN_euler(lista):
    for el in lista:
        t_lista = euler(0, 4, el, 20)[0]
        y_lista = euler(0, 4, el, 20)[1]
        plt.plot(t_lista, y_lista, label=str(el))
    plt.plot(euler(0, 4, 10000, 20)[0], euler(0, 4, 10000, 20)[3], 'r', label='Analiticki')
    plt.legend(loc="lower left")
    plt.grid()
    plt.show()

def periodi_razN_RK4(lista):
    for el in lista:
        t_lista = RK4(0, 4, el, 20)[0]
        y_lista = RK4(0, 4, el, 20)[1]
        plt.plot(t_lista, y_lista, label=str(el))
    plt.legend(loc="lower left")
    plt.grid()
    plt.show()

# periodi_razN_euler(listN)
# periodi_razN_RK4(listN)






def N_razMetoda():
    fig, ax = plt.subplots()
    ax.grid()
    plt.plot(euler(0, 4, 200000, 20)[0],  euler(0, 4, 200000, 20)[3], label='sin y = y')
    plt.plot(euler(0, 4, 200000, 20)[0],  euler(0, 4, 200000, 20)[1], label='Euler')
    plt.plot(RK4(0, 4, 200000, 20)[0],  RK4(0, 4, 200000, 20)[1], label='RK4')
    ax.set_xlim([19, 20])
    # ax.set_ylim([0, 1])
    plt.legend(loc="lower left")
    plt.show()

# N_razMetoda()






kutevi = [4, 8, 16, 32, 64]

def periodi_razPU_RK4(lista):
    for el in lista:
        t_lista = RK4(0, el, 10000, 20)[0]
        y_lista = RK4(0, el, 10000, 20)[1]
        plt.plot(t_lista, y_lista, label=str(el))
    plt.legend(loc="lower left")
    plt.xlim([0, 7])
    plt.grid()
    plt.show()

periodi_razPU_RK4(kutevi)









# vx, vy, vz = [], [], []
# ax, ay, az = [], [], []
# x, y, z = [], [], []


# vx[i] = vx[i-1] + ax[i-1]*h
# vy[i] = vy[i-1] + ay[i-1]*h
# vz[i] = vz[i-1] + az[i-1]*h

# x[i] = x[i-1] + vx[i-1]*h + 1/2*ax[i-1]*h**2
# y[i] = y[i-1] + vy[i-1]*h + 1/2*ay[i-1]*h**2
# z[i] = z[i-1] + vz[i-1]*h + 1/2*az[i-1]*h**2