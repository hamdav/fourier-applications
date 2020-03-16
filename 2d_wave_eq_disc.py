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

n = 100
phis = np.linspace(0,2*np.pi,n)

times = np.linspace(0,1,100)

# Define the initial function f(r)
f = lambda rs: np.exp(-rs)

# Define the square root of the lambda_ms
m = 10
sqls = spec.jn_zeros(0,m)/rho
# Define the bms from f and the bessel function
bms = np.trapz(f(rs)[:,np.newaxis] * spec.j0(np.outer(rs, sqls)),
               axis=0, dx=dr)/ np.trapz(spec.j0(np.outer(rs, sqls))**2,
               axis=0, dx=dr)

def ufcn(t):
    # Returns matrix of u with the element at n,m being u(r_n,phi_m,t)
    Tms = np.cos(sqls * c*t)
    Rms = spec.j0(np.outer(rs, sqls))
    Phis = np.ones(len(phis))
    bmsRmsTms = bms[np.newaxis,:] * Tms[np.newaxis,:] * Rms
    return np.outer(Phis,np.sum(bmsRmsTms, axis=1))


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
dAngle = 0.05

def animate(i):
    t = times[i]
    angle = dAngle*i
    us = ufcn(t)
    ax.clear()
    surf = ax.plot_surface(X,Y,us,cmap='plasma', norm=norm)
    ax.set_zlim([-limit,limit])
    ax.view_init(elev=30., azim=angle)
    return surf,

anim = FuncAnimation(fig, animate, init_func=None, frames = len(times), interval=10, blit=False, repeat=True, repeat_delay=0)

# Set up formatting for the movie files
Writer = animation.writers['imagemagick']
writer = Writer(fps=15, bitrate=1800)

anim.save('2dwave_on_disk.gif',writer=writer)


