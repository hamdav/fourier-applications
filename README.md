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
u(x,0) = f(x), u_t (x,0) = 0
or
u(x,0) = 0, u_t (x,0) = f(x).
and boundry conditions some combination of either
u(0,t) = 0 or u_t (0,t) = 0, and
u(l,t) = 0 or u_t (l,t) = 0.

