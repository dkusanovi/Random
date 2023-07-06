import matplotlib.pyplot as plt
import numpy as np
import math

class Planet:
    def __init__(self, name, mass, xy, v, color):
        self.name = name
        self.mass = mass
        self.xy = xy
        self.v = v
        self.color = color
        self.x = [xy[0]]
        self.y = [xy[1]]
        self.a = np.array([0, 0])
        

class Satelite:
    def __init__(self, name, mass, xy, v, color):
        self.name = name
        self.mass = mass
        self.xy = xy
        self.v = v
        self.color = color
        self.xx = [xy[0]]
        self.yy = [xy[1]]
        self.a = np.array([0, 0])
        


class Universe:
    def __init__(self):
        self.planets = []
        self.satelites = []
        self.G = 6.67408*10**(-11)
        self.t = 0


    def add_planets(self, p):
        self.planets.append(p)

    def add_satelites(self, s):
        self.satelites.append(s)
                

    def __move(self, dt):
            self.t = self.t + dt

            for some_planet in self.planets:
                some_planet.a = np.array([0, 0])
                for some_other_planet in self.planets:
                    if some_planet != some_other_planet:
                        d = (some_planet.xy - some_other_planet.xy)**2
                        n = math.sqrt(d[0] + d[1])
                        some_planet.a = some_planet.a - self.G*(some_other_planet.mass / n**3 )*(some_planet.xy - some_other_planet.xy)

                some_planet.v = some_planet.v + some_planet.a*dt
                some_planet.xy = some_planet.xy + some_planet.v*dt

                some_planet.x.append(some_planet.xy[0])
                some_planet.y.append(some_planet.xy[1])


    def __move_satelites(self, dt):
            self.t = self.t + dt

            for some_satelite in self.satelites:
                some_satelite.a = np.array([0, 0])
                for some_satelite in self.satelites:
                        if some_satelite != self.planets[3]:
                            d = (some_satelite.xy - self.planets[3].xy)**2
                            n = math.sqrt(d[0] + d[1])
                            some_satelite.a = some_satelite.a - self.G*(self.planets[3].mass / n**3 )*(some_satelite.xy - self.planets[3].xy)

                some_satelite.v = some_satelite.v + some_satelite.a*dt
                some_satelite.xy = some_satelite.xy + some_satelite.v*dt

                some_satelite.xx.append(some_satelite.xy[0])
                some_satelite.yy.append(some_satelite.xy[1])

        
    def evolve(self, tuk, dt):
            step = round(tuk/dt)
            br = 0
            while br < step:
                self.__move(dt)
                br = br + 1
            x, y = [], []
            for some_planet in self.planets:
                x.append(some_planet.x)
                y.append(some_planet.y)

            return x, y


    def evolve_satelite(self, tuk, dt):
            step = round(tuk/dt)
            br = 0
            while br < step:
                self.__move_satelites(dt)
                br = br + 1
            xx, yy = [], []
            for some_satelite in self.satelites:
                xx.append(some_satelite.xx)
                yy.append(some_satelite.yy)

            return xx, yy