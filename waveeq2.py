import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PI = 3.14159265358979
c = 0.3

fig,ax = plt.subplots()

startt = -10
endt = 10
n = 1000
dt = (endt-startt)/n
times = np.linspace(startt,endt,n)

startx = -10
endx = 10
n = 1000
dx = (endx-startx)/n
xs = np.linspace(startx,endx,n)


# Write f such that it takes a numpy array of x-values and returns a numpy array
# OBS! If f returns a regular python list, things will end badly
# See below for the interpretation of f

    # Gauss
#f = lambda xs: np.exp(-xs**2)
    # Two Gausses
#f = lambda xs: np.exp(-(xs-5)**2) + np.exp(-(xs+5)**2)
    # Heaviside
#f = lambda xs: np.array([int(x < 0) for x in xs])
    # Spikes
#f = lambda xs: np.where(np.abs(np.mod(xs,4)-2)-1.5 > 0, np.abs(np.mod(xs,4)-2)-1.5, np.zeros(xs.shape))
    # Photon
f = lambda xs: np.exp(-xs**2)*np.cos(10*xs)


# Define ufcn based on the initial condition

    # Initial condition , u(x,0) = f(x), d/dt u(x,0) = 0
ufcn = lambda t: f(xs-c*t) + f(xs+c*t)

    # Initial condition, u(x,0) = 0, d/dt u(x,0) = f'(x)
#ufcn = lambda t: 0.5*(f(xs+c*t) - f(xs-c*t))

us = ufcn(0)

line, = ax.plot(xs,us,'k')
ax.set_ylim([-1,1])

def animate(t):
    us = ufcn(t)
    line.set_ydata(us)
    line.set_color('r')
    return line,

anim = FuncAnimation(fig,animate,init_func=None,frames = times, interval=10,blit=True,repeat=True, repeat_delay=0)

plt.show()
