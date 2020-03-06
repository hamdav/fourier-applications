import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PI = 3.14159265358979
c = 1


fig,ax = plt.subplots()

fintime = 10
dt = 0.01
n = int(fintime/dt +1)
times = np.linspace(-fintime,fintime,n)

maxx = 10
dx = 0.01
n = int(maxx*2/0.01 + 1)
xs = np.linspace(-maxx,maxx,n)

#f = lambda xs: np.exp(-xs**2)
#f = lambda xs: np.exp(-(xs-5)**2) + np.exp(-(xs+5)**2)
#f = lambda xs: np.array([int(x < 0) for x in xs])
# Taggar
#f = lambda xs: np.where(np.abs(np.mod(xs,4)-2)-1.5 > 0, np.abs(np.mod(xs,4)-2)-1.5, np.zeros(xs.shape))
f = lambda xs: np.exp(-xs**2)*np.cos(10*xs)

# Initial condition, u(x,0) = f(x), d/dt u(x,0) = 0
#ufcn = lambda t: f(xs-c*t) + f(xs+c*t)

# Initial condition, u(x,0) = 0, d/dt u(x,0) = f'(x)
ufcn = lambda t: 0.5*(f(xs+c*t) - f(xs-c*t))

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
