import math
#Newtons_method
def Newtons_method(p0, f, f_prime):
    tol = 1e-4
    maxiter= 100
    i = 1
    while i < maxiter:
        p = p0 - f(p0)/f_prime(f, p0)
        if abs(p - p0) < tol:
            return p, i
        p0 = p
        i += 1
    return "No solution found"

def f_prime(f, x):
    tol = 1e-4
    return (f(x + tol) - f(x))/tol

def f1(x):
    return x**3 - 2*x**2 - 5

def f2(x):
    return x**2 - 2*x*math.exp(-x) + math.exp(-2*x)
def f3(x):
    return x**3 -3*(x**2)*(2**(-x)) + 3*x*(4**(-x)) - 8**(-x)   

print("Answer 3")
print(Newtons_method(1, f1, f_prime))
print(Newtons_method(0.5, f2, f_prime))
print(Newtons_method(0.5, f3, f_prime))
