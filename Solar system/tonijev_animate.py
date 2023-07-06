import tonijev_universe as universe
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

au = 1.496e11
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun","yellow", 1.989e30, np.array((0.,0.)), np.array((0.,0.)))
mercury = universe.Planet("Mercury","orange", 3.3e24, np.array((0.,0.466 * au)), np.array((-47362.,0.)))
venus = universe.Planet("Venus","red", 4.8685e24, np.array((0.723 * au,0.)), np.array((0.,35020.)))
earth = universe.Planet("Earth","blue", 5.9742e24, np.array((-1.*au,0.)), np.array((0.,-29783.)))
mars = universe.Planet("Mars", "brown", 6.417e23, np.array((0.,-1.666 * au)), np.array((24007.,0.)))

ss = universe.Universe()
ss.add_planet(sun)
ss.add_planet(mercury)
ss.add_planet(venus)
ss.add_planet(earth)
ss.add_planet(mars)

ss.evolve(5*year)

# First set up the figure, the axis
fig = plt.figure()
ax = plt.axes(xlim=(-2*au, 2*au), ylim=(-2*au, 2*au))

# Draw trajectories
plt.plot(mercury.x,mercury.y,label=mercury.name,color=mercury.color)
plt.plot(venus.x,venus.y,label=venus.name,color=venus.color)
plt.plot(earth.x,earth.y,label=earth.name,color=earth.color)
plt.plot(mars.x,mars.y,label=mars.name,color=mars.color)
plt.legend(loc="upper right")

# Prepare lines that will be animated
lines = []
planets = [sun, mercury, venus, earth, mars]

for p in planets:
    lobj = ax.plot([], [], 'o', color=p.color)[0]
    lines.append(lobj)

# initialization function
def init():
    for line in lines:
        line.set_data([],[])
    return lines

# animation function.  This is called sequentially
def animate(i):
    for index, p  in enumerate(planets):
        x = p.x[i]
        y = p.y[i]
        lines[index].set_data(x, y)
    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=int(2*year/(0.1*day)), interval=10, blit=True)

plt.show()