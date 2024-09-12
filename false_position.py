import math
import matplotlib.pyplot as plt
import numpy as np
#False_Position

def false(f, p0, p1):
    tol = 1e-4
    maxiter = 1000
    i = 2
    f_p0 = f(p0)
    f_p1 = f(p1)
    if f_p0 * f_p1 > 0:
        return "Method fails"
    while i < maxiter:
        if f_p1 - f_p0 == 0:
            return "Division by zero error"
        c = (p0 * f_p1 - p1 * f_p0) / (f_p1 - f_p0)
        f_c = f(c)
        if f_p0 * f_c < 0:
            p1 = c
            f_p1 = f_c  
        else:
            p0 = c
            f_p0 = f_c  
        if f_c == 0 or abs(f_c) < tol:
            return c, i
        i += 1
    return p0 - f(p0)*(p1 - p0)/(f(p1) - f(p0)) 
def f(x):   
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9

print("Answer 4")
print(false(f, -1, 0))
print(false(f, 0, 2))