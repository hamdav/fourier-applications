import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
import scipy.special as spec

c = 1

rho = 1
n = 100
dr = rho/n
rs = np.linspace(0,rho,n)

n = 74
phis = np.linspace(0,2*np.pi,n)

times = np.linspace(0,8,400)

# Define the initial function f(r)
f = lambda rs: np.exp(-5*rs)* np.cos(np.pi*rs/(2*rho))
#f = lambda rs: np.cos(3*np.pi*rs/(2*rho))
#f = lambda rs: 1-rs

# Define the square root of the lambda_ms
m = 53
sqls = spec.jn_zeros(0,m)/rho
# Define the bms from f and the bessel function
bms = 2 * np.trapz(rs[:,np.newaxis] * f(rs)[:,np.newaxis] * spec.j0(np.outer(rs, sqls)),
               axis=0, dx=dr)/ (rho**2 * spec.j1(spec.jn_zeros(0,m))**2)


def ufcn(t):
    # Returns matrix of u with the element at n,m being u(r_n,phi_m,t)
    Tms = bms * np.cos(sqls * c*t)
    Rms = spec.j0(np.outer(sqls,rs))
    Phis = np.ones(len(phis))
    bmsRmsTms = Tms[:,np.newaxis]*Rms
    #breakpoint()
    return np.outer(Phis,np.sum(bmsRmsTms, axis=0))


u0 = ufcn(0)

limit = max(np.abs(np.max(np.max(u0))),np.abs(np.min(np.min(u0))))
norm = cm.colors.Normalize(vmax=limit, vmin=-limit)

# Surf plot figure

fig = plt.figure(1)
ax = fig.add_subplot(111,projection='3d')

# Create a mesh of rs and phis
R, P = np.meshgrid(rs,phis)

# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)

# Plot the surface
surf = ax.plot_surface(X,Y,u0)

# How much to rotate per frame
dAngle = 1.00

def animate(i):
    t = times[i]
    angle = dAngle*i
    us = ufcn(t)
    ax.clear()
    surf = ax.plot_surface(X,Y,us,cmap='gnuplot2', norm=norm)
    ax.set_zlim([-limit,limit])
    ax.view_init(elev=20., azim=angle)
    return surf,

anim = FuncAnimation(fig, animate, init_func=None, frames = len(times), interval=10, blit=False, repeat=True, repeat_delay=0)

# Set up formatting for the movie files
Writer = animation.writers['imagemagick']
writer = Writer(fps=15, bitrate=1800)

anim.save('2dwave_on_disk.gif',writer=writer)


