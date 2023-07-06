import math
import numpy as np

class Planet:
    def __init__(self, name, color, m, r, v):
        self.name = name
        self.color = color
        self.m    = m
        self.r    = r
        self.v    = v
        self.a    = np.array((0.,0.))
        self.x = []
        self.y = []
        self.dr = []

        self.x.append(r[0])
        self.y.append(r[1])

class Universe:
    G = 6.67408e-11
    day = 60*60*24
    def __init__(self, dt=0.1):
        self.planets = []
        self.dt = dt * self.day
        self.t = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def evolve(self, time, method = 'euler'):
        self.t.append(0)
        steps = int(time/self.dt)
        #steps = 4
        i=1
        while i < steps:
            self.__move()
            i += 1

    def __total_mass(self):
        M = 0
        for p in self.planets:
            M += p.m
        return M

    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        # Calculate distances between all planets
        for p1 in self.planets:
            p1.dr.clear()
            for p2 in self.planets:
                if (p1 == p2):
                    p1.dr.append(np.array((0.,0.)))
                else:
                    p1.dr.append((-1*self.G*p2.m*(p1.r - p2.r))/(np.linalg.norm(p1.r - p2.r))**3)

            # Move plantes
            p1.a *= 0
            for dr in p1.dr:
                p1.a = p1.a + dr

            #print(p1.name,p1.a)
            p1.v = p1.v + p1.a*self.dt
            p1.r = p1.r + p1.v*self.dt

            #print(p1.name, p1.r)
            p1.x.append(p1.r[0])
            p1.y.append(p1.r[1])