# Secant mMethod

import numpy as np
import matplotlib.pyplot as plt

def Secant(f, a, b):
    N = 1000
    tol = 1.0e-10
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0 or abs(f_m_n) < tol:
            return m_n, n
        else:
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
 

def f(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9

print("Answer 4")
print(Secant(f, -1, 0))
print(Secant(f, 0, 1))
     