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


