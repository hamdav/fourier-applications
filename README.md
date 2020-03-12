# fourier-applications

## wave_eq_on_R.py

Creates an animation of the solution to the wave equation on the real line, 
u_{tt} = c^2 u_{xx},
with initial conditions either 
u(x,0) = f(x), u_t (x,0) = 0
or
u(x,0) = 0, u_t (x,0) = f(x).

## wave_eq_bounded.py

Creates an animation of the solution to the wave equation on the bounded interval [0,l],
u_{tt} = c^2 u_{xx},
with initial conditions either
1. u(x,0) = f(x), u_t (x,0) = 0, or
2. u(x,0) = 0, u_t (x,0) = f(x).

and the two boundry conditions are

i) u(0,t) = 0 or

ii) u_t (0,t) = 0

and

i) u(l,t) = 0 or

ii) u_t (l,t) = 0.

If the initial conditions are 1,
then 

    u(x,0) = \sum bn sin(n π x /l) = f(x) or 

    u(x,0) = \sum bn sin((n+1/2) π x/l) = f(x) or

    u(x,0) = \sum bn cos((n+1/2) π x/l) = f(x) or

    u(x,0) = \sum bn cos(n π x /l) = f(x).

If on the other hand initial conditions are 2, then 

    u_t (x,0) = \sum bn n π c / l * sin(n π x /l) = f(x) or 

    u_t (x,0) = \sum bn (n+1/2) π c/l * sin((n+1/2) π x/l) = f(x) or

    u_t (x,0) = \sum bn (n+1/2) π c/l * cos((n+1/2) π x/l) = f(x) or

    u_t (x,0) = \sum bn n π c / l * cos(n π x /l) = f(x).

These bn are the ones you need to calculate to create the animation. 
This should probably be done by expanding f(x) into a fourier series.

## 2d_wave_eq_square.py

Creates an animation of the solution to the two dimensional wave equation on the bounded interval [0,1]x[0,1],
u_{tt} = c^2 (u_{xx} + u_{yy},
with initial conditions either
1. u(x,y,0) = f(x,y), u_t (x,0) = 0, or
2. u(x,0) = 0, u_t (x,0) = f(x).

and the boundry conditions 

i) u(0,y,t) = 0 

ii) u(1,y,t) = 0

iii) u(x,0,t) = 0, and

iv) u(x,1,t) = 0.


When solving this you get an expression like

u(x,y,t) = \sum_{n,m} a_{n,m} sin(π t \sqrt{n^2+m^2}) * sin(n π x) * sin(m π y)

these a_{n,m}:s are the ones you need to calculate from the initial condition if you want to create an animation not already calculated by me.

OBS! This creates a gif file as the animation is very slow and without a considerable drop in framerate cannot be played in realtime.
