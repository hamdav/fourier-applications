import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time

xmin = 0; xmax = 1; n = 100
xs = np.linspace(xmin, xmax, n)
ymin = 0; ymax = 1; n = 100
ys = np.linspace(ymin, ymax, n)
times = np.linspace(0,5,200)

(X,Y) = np.meshgrid(xs,ys)

ns = np.array(range(0,20))
ms = np.array(range(0,20))

# anms calculated from initial condition
anms = np.zeros((len(ns),len(ms)))
    # Sinusoidal anms: set anms zero and anms[j][k] = some constant
    # to get initial condition f(x,y) = sin( pi j x) * sin( pi k y)
    # These can be added by setting multiple anms to constants
#anms[4][4] = 1/16
#anms[2][3] = 1/4
#anms[1][1] = 1
#anms[2][2] = 1/8

    # sin(pi x) * sin(4 pi x) * sin(pi y) * sin(4 pi y)
#for n in ns:
    #for m in ms:
        #if n%2==0 and m%2==0:
            #anms[n][m] = 16*n/(np.pi*(n**4 -34*n**2 + 225))* 16*m/(np.pi*(m**4 -34*m**2 + 225))



f = lambda x,y: (x**2-x)*(y**2-y) 
integralxs = np.linspace(0,1,100)
integralys = np.linspace(0,1,100)
anmfunc = lambda n, m: np.trapz(np.trapz(
    f(integralxs, integralys) * np.outer(np.sin(n*np.pi*integralys),
                                         np.sin(m*np.pi*integralys)),
    dx =0.01),dx=0.01)

for n in ns:
    for m in ms:
        anms[n][m] = anmfunc(n,m)

print(f"Time taken for anms: {e-s}")

def ufcn(t):
    Tnm = np.cos(np.pi*np.sqrt(np.add.outer(ns**2,ms**2))*t)
    subexp_1 = np.multiply(Tnm, anms)
    Xns = np.sin(np.pi*np.outer(ns,xs))
    Yms = np.sin(np.pi*np.outer(ms,ys))
    XnsYms = np.multiply.outer(Xns,Yms)
    nsmsXsYs = np.swapaxes(XnsYms,1,2)
    fourDArr = subexp_1[:,:,np.newaxis,np.newaxis]*nsmsXsYs
    return np.sum(np.sum(fourDArr,axis=0),axis=0)


u0 = ufcn(0)

limit = max(np.abs(np.max(np.max(u0))),np.abs(np.min(np.min(u0))))
norm = cm.colors.Normalize(vmax=limit, vmin=-limit)

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
    surf = ax2.plot_surface(X,Y,us,cmap='plasma', norm=norm)
    ax2.set_zlim([-limit,limit])
    ax2.view_init(elev=20., azim=i)
    return surf,

anim2 = FuncAnimation(fig2, animate, init_func=None, frames = len(times), interval=10, blit=False, repeat=True, repeat_delay=0)

# Set up formatting for the movie files
Writer = animation.writers['imagemagick']
writer = Writer(fps=15, bitrate=1800)

anim2.save('2dwave.gif',writer=writer)

# Do not show this figure, it is rather slow, instead look at the gif
plt.close()

# Imshow figure

fig = plt.figure(1)
ax = fig.add_subplot(111)

im = ax.imshow(u0,norm=norm)

def animate(t):
    us = ufcn(t)
    im.set_data(us)
    return im,


anim = FuncAnimation(fig,animate,init_func=None,frames = times, interval=10,blit=True,repeat=True, repeat_delay=0)



plt.show()
