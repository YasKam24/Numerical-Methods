import sympy as sp
import math
#Gauss Qudrature

#One Point Gauss Quadrature

def f(x):
    return (x**2)*(math.sin(x))

def one_point_gaussian_quadrature(f, a, b):
    mid = (a + b) / 2
    return 2 * (f(mid)) * mid

def two_point_gaussian_quadrature(f, a, b):
    mid = (a + b) / 2
    return f(mid - (1 / math.sqrt(3))) + f(mid + (1 / math.sqrt(3)))

x = sp.Symbol('x')
f1 = (x**2) * sp.sin(x)

integerate = sp.integrate(f1, (x, 0, math.pi/4))
print(integerate)
print(one_point_gaussian_quadrature(f, 0, math.pi/4))