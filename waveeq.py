import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PI = 3.14159265358979
c = 1
l = 1

# C0 is -pi/2, cn is -2/npi if n is odd, 0 otherwise
ns = np.array(range(1,1000))
# For u0(x) = abs(x/l-1/2)-1/2
bns = np.array([4*l/PI**2*(PI/(2*n)*np.cos(n*PI/2)-np.sin(n*PI/2)/n**2) if n%2==1 else 0 for n in ns])

# For u0(x) = plucked att l/10
#bns = -2/PI*(100/(9*PI)*np.sin(ns*PI/10)/ns**2)

#For u0(x) = sin(2*pi x/l)
#bns = 1*(ns==3)


u0_fourier_test = lambda x: sum(bns*np.sin(ns*PI*x/l))


u = lambda x,t: sum(bns*np.cos(c*ns*PI*t/l)*np.sin(ns*PI*x/l))

figinit,axinit = plt.subplots()
fig,ax = plt.subplots()

time = 0
dt = 0.01
xs = np.linspace(0,l,100)

us = [u(x,0) for x in xs]

axinit.plot(xs,us)

line, = ax.plot(xs,us,'k')
ax.set_ylim([-1,1])

def animate(i):
    time = dt*i
    us = [u(x,time) for x in xs]
    line.set_ydata(us)
    line.set_color('r')
    return line,

anim = FuncAnimation(fig,animate,init_func=None,interval=10,blit=True,frames=200,repeat=True, repeat_delay=0)


plt.show()
