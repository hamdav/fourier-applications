import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

xmin = 0; xmax = 1; n = 100
xs = np.linspace(xmin, xmax, n)
ymin = 0; ymax = 1; n = 100
ys = np.linspace(ymin, ymax, n)

(X,Y) = np.meshgrid(xs,ys)

ns = np.array(range(0,10))
ms = np.array(range(0,11))

anms = np.zeros((len(ns),len(ms)))
anms[2][2] = 1/4

def outer_along_first_axis(nxs, mys):
    # Takes two arrays with u-values with different n values on 0th axis and different x/y values on 1st axis. 
    # Returns ns on first axis, ms on second axis and the elementwise products of x and ys on third axis
    return nxs[np.newaxis,:,:]*mys[:,np.newaxis,:]

#ufcn = lambda t: np.sum(np.sum(anms[:,:,np.newaxis]*np.cos(np.pi*np.sqrt(np.add.outer(ns**2,ms**2))*t)[:,:,np.newaxis]* outer_along_first_axis(np.sin(np.pi*np.outer(ns,xs)),np.sin(np.pi*np.outer(ms,ys)))))
def ufcn(t):
    Tnm = np.cos(np.pi*np.sqrt(np.add.outer(ns**2,ms**2))*t)
    subexp_1 = np.multiply(Tnm, anms)
    Xns = np.sin(np.pi*np.outer(ns,xs))
    Yms = np.sin(np.pi*np.outer(ms,ys))
    XnsYms = np.multiply.outer(Xns,Yms)
    nsmsXsYs = np.swapaxes(XnsYms,1,2)
    fourDArr = subexp_1[:,:,np.newaxis,np.newaxis]*nsmsXsYs
    #breakpoint()
    return np.sum(np.sum(fourDArr,axis=0),axis=0)


u0 = ufcn(0)


# Imshow figure

fig = plt.figure(1)
ax = fig.add_subplot(111)

limit = max(np.abs(np.max(np.max(u0))),np.abs(np.min(np.min(u0))))
norm = cm.colors.Normalize(vmax=limit, vmin=-limit)
im = ax.imshow(u0,norm=norm)

def animate(t):
    us = ufcn(t)
    im.set_data(us)
    return im,

times = np.linspace(0,2,100)

#anim = FuncAnimation(fig,animate,init_func=None,frames = times, interval=10,blit=True,repeat=True, repeat_delay=0)


# Surf plot figure

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111,projection='3d')

surf = ax2.plot_surface(X,Y,u0)

# How much to rotate per frame
dAngle = 1

def animate(i):
    t = times[i]
    angle = dAngle*i
    us = ufcn(t)
    ax2.clear()
    surf = ax2.plot_surface(X,Y,us,cmap='hot', norm=norm)
    ax2.set_zlim([-limit,limit])
    ax2.view_init(elev=20., azim=i)
    return surf,

anim = FuncAnimation(fig2, animate, init_func=None, frames = len(times), interval=10, blit=False, repeat=True, repeat_delay=0)

# Set up formatting for the movie files
Writer = animation.writers['imagemagick']
writer = Writer(fps=15, bitrate=1800)

anim.save('test.gif',writer=writer)

plt.show()
