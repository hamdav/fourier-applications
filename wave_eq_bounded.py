import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PI = 3.14159265358979
c = 1
l = 1

# The ns that will be used
ns = np.array(range(1,100))


# Create bns as fourier coefficients for f(x)


    # For u0(x) = abs(x/l-1/2)-1/2
#bns = np.array([4*l/PI**2*(PI/(2*n)*np.cos(n*PI/2)-np.sin(n*PI/2)/n**2) if n%2==1 else 0 for n in ns])

    # For u0(x) = plucked att l/10
#bns = -2/PI*(100/(9*PI)*np.sin(ns*PI/10)/ns**2)

    # For u0(x) = sin(2*pi x/l)
bns = 1*(ns==3)


# Define a function as a partial sum
    # If initial conditions are 1)
T = lambda t: np.cos(c*ns*PI*t/l)
    # If initial conditions are 2)
#T = lambda t: np.sin(c*ns*PI*t/l)

    # If boundry conditions are i) and i)
#X = lambda x: np.sin(ns*PI*x/l)
    # If boundry conditions are i) and ii)
#X = lambda x: np.sin((ns+1/2)*PI*x/l)
    # If boundry conditions are ii) and i)
#X = lambda x: np.cos((ns+1/2)*PI*x/l)
    # If boundry conditions are ii) and ii)
X = lambda x: np.cos(ns*PI*x/l)


u = lambda x,t: sum(bns*T(t)*X(x))



fig,ax = plt.subplots()

startt = 0
endt = 10
n = 1000
dt = (endt-startt)/n
times = np.linspace(startt,endt,n)

n = 1000
xs = np.linspace(0,l,n)

us = [u(x,0) for x in xs]


line, = ax.plot(xs,us,'k')
ax.set_ylim([-1,1])


def animate(t):
    us = [u(x,t) for x in xs]
    line.set_ydata(us)
    line.set_color('r')
    return line,


anim = FuncAnimation(fig,animate,init_func=None,interval=10,blit=True,frames=times,repeat=True, repeat_delay=0)

plt.show()
