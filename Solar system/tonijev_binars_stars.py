import universe
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

au = 1.496e11
day = 60*60*24
year = 365.242*day

sun1 = universe.Planet("Sun","yellow", 1.989e30, np.array((0.,0.)), np.array((0.,-10000.)))
sun2 = universe.Planet("Sun","orange", 1.989e30, np.array((0.1*au,0.)), np.array((0.,10000.)))

ss = universe.Universe()
ss.add_planet(sun1)
ss.add_planet(sun2)

ss.evolve(0.5*year)

# First set up the figure, the axis
fig = plt.figure()
ax = plt.axes(xlim=(-1*au, 1*au), ylim=(-1*au, 1*au))

# Draw trajectories
plt.plot(sun1.x,sun1.y,label=sun1.name,color=sun1.color)
plt.plot(sun2.x,sun2.y,label=sun2.name,color=sun2.color)
plt.legend(loc="upper right")

# Prepare lines that will be animated
lines = []
planets = [sun1, sun2]

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