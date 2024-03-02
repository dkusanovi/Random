# Cilj : odrediti jednadžbe stanja bijelih patuljaka 
# za dobiti njihove strukture
# ovisnost mase i gustoce o radijusu bijelog patuljka
# ovisnost dmdr i drhodr


import math
import matplotlib.pyplot as plt

G = 6.6743 * 10**(-11)                         # gravitational constant
mp = 1.67 * 10**(-27)                          # proton mass [kg]
me = 9.11 * 10**(-31)                          # electron mass [kg]
Ye = 1
c = 3 * 10**8                                  # speed of light in vacuum
h = 6.626 * 10**(-34)                          # planck

Ms = 1.989 * 10**30                            # mass of the Sun [kg]
Rs = 6.9634*  10**8                            # radius of the Sun [m]

n0 = (8*math.pi*(me**3)*(c**3))/(3*(h**3))
rho0 = (mp*n0)/Ye
rho = 8 * 10**10
mmax = 1.44*Ms                                 # max mass, if > collaps
rhomax = 10**(-1)                              # max central density
h1 = 100                                       # step
m0 = m = 0
r = 0.0001


def gamma(rho, rho0):
    x = (rho/rho0)**(1/3)
    return (x**2)/(3*math.sqrt(1+x**2))

def dmdr(r, rho):
    return 4*math.pi*r**2*rho

def drhodr(r, m, rho, rho0):
    return -(G*m*rho*mp)/((r**2)*me*Ye*(c**2)*gamma(rho, rho0))


def RK4(r0, m0):
    mass = [m0]
    density = [rho0]           # the range is 10**(-1) to 10**6, reverse
    rlist = [r0]

    while (density[-1] >= rhomax and mass[-1] <= mmax):
        R = rlist[-1]
        D = density[-1]
        M = mass[-1]


        km1 = dmdr(R, D)
        krho1 = drhodr(R, M, D, rho0)

        km2 = dmdr(R, D + krho1*h1/2)
        krho2 = drhodr(R, M + km1*h1/2, D + krho1*h1/2, rho0)

        km3 = dmdr(R, D + krho2*h1/2)
        krho3 = drhodr(R, M + km2*h1/2, D + krho2*h1/2, rho0)

        km4 = dmdr(R, D + krho3*h1)
        krho4 = drhodr(R, M + km3*h1, D + krho3*h1, rho0)

        rlist.append(R+h1)
        mass.append(M + 1/6*(km1 + 2*km2 + 2*km3 + km4)*h1)
        density.append(D + 1/6*(krho1 + 2*krho2 + 2*krho3 + krho4)*h1)

    return rlist, mass, density


rlist, mass, density = RK4(r, m0)


def mass_graph():
    fig, ax = plt.subplots()
    ax.grid()
    plt.plot(rlist, mass)
    plt.xlabel('radius [m]')
    plt.ylabel('mass [kg]')
    fig.savefig("mass.png")
    plt.show()


def density_graph():
    fig, ax = plt.subplots()
    ax.grid()
    plt.plot(rlist, density, label="density")
    # plt.legend(loc="lower left")
    plt.xlabel('radius [m]')
    plt.ylabel('density [kg/m$^3$]')
    fig.savefig("density.png")
    plt.show()


mass_graph()
density_graph()









# sve sljedece bi bilo dobro da je raden bezdimenzionalni model
# tad r i m imaju malo drukciju ovisnost pa bi se tocke poklapale


# def mass_graph_stein():
#     fig, ax = plt.subplots()
#     ax.grid()
#     plt.plot(rlist, mass)
#     x3, y3 = (Rstein, Mstein)
#     plt.scatter(x3, y3, label='Stein 2051 DC', color='green')      # Ye = 1
#     plt.xlabel('radius [m]')
#     plt.ylabel('mass [kg]')
#     plt.legend(loc="upper left")
#     fig.savefig("mass_stein.png")
#     plt.show()

# def mass_graph_sirius_stein():
#     fig, ax = plt.subplots()
#     ax.grid()
#     plt.plot(rlist, mass)
#     x1, y1 = (Rsirius, Msirius)
#     x2, y2 = (Rstein, Mstein)
#     plt.scatter(x2, y2, label='Stein 2051 DC', color='green')      # Ye = ?
#     plt.scatter(x1, y1, label='Sirius B DA', color='orange')        # Ye = 1
#     plt.xlabel('radius [m]')
#     plt.ylabel('mass [kg]')
#     plt.legend(loc="upper left")
#     fig.savefig("mass_sirius_stein.png")
#     plt.show()

# mass_graph_stein()
# mass_graph_sirius_stein()

# Mprocyon, Rprocyon = 0.63*Ms, 0.01234*Rs     # Procyon B
# Mvanmaanen, Rvanmaanen = 0.68*Ms, 0.011*Rs   # Van Maanen 2
# Mlp, Rlp = 0.61*Ms, 0.01*Rs                  # LP 145-41
# Mg, Rg = 0.81*Ms, 0.00984*Rs                 # G 240-72

# def mass_graph_all():
#     fig, ax = plt.subplots()
#     ax.grid()
#     plt.plot(rlist, mass)
#     x1, y1 = (Rsirius, Msirius)
#     x2, y2 = (Reri, Meri)
#     x3, y3 = (Rstein, Mstein)
#     x4, y4 = (Rprocyon, Mprocyon)
#     x5, y5 = (Rvanmaanen, Mvanmaanen)
#     x6, y6 = (Rlp, Mlp)
#     x7, y7 = (Rg, Mg)
#     plt.scatter(x1, y1, label='Sirius B DA')        # Ye = 1
#     plt.scatter(x2, y2, label='40 Eri B DA')        # Ye = 1
#     plt.scatter(x3, y3, label='Stein 2051 DC')      # Ye = ?
#     plt.scatter(x4, y4, label='Procyon B DQZ')      # Ye = 1 or 0.5 
#     plt.scatter(x5, y5, label='Van Maanen 2 DZ')    # Ye = 0.5
#     plt.scatter(x6, y6, label='LP 145-41 DQ')       # Ye = 1
#     plt.scatter(x7, y7, label='G 240-72 DQ')        # Ye = 1
#     plt.xlabel('radius [m]')
#     plt.ylabel('mass [kg]')
#     plt.legend(loc="upper left")
#     plt.show()

# mass_graph_all()