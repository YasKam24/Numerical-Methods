
import math
#Rectangular Method

def rectangular(f, a, b):
    return f(a) * (b - a)

def midpoint(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

def trapezoidal(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

def simpsons(f, a, b):
    h = (b - a)/2
    return h/3 * (f(a) + f(b) + 4*f(a + h))

print(rectangular(lambda x : (1 + x**2)**0.5, 1, 5))
print(midpoint(lambda x : (1 + x**2)**0.5, 1, 5))
print(trapezoidal(lambda x : (1 + x**2)**0.5, 1, 5))
print(simpsons(lambda x : (1 + x**2)**0.5, 1, 5))
print(trapezoidal(lambda x: 2/(x - 4), 0, 0.5))
print(simpsons(lambda x: 2/(x - 4), 0, 0.5))
print(simpsons(lambda x: math.exp(3*x)*math.sin(2*x), 0, math.pi/4))
print(trapezoidal(lambda x: math.exp(3*x)*math.sin(2*x), 0, math.pi/4))