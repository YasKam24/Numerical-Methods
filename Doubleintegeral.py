
import numpy as np
def simpsons_double_integral(f, a, b, c, d, m, n):
    h = (b - a) / n  # Step 1: Calculate h
    J1 = J2 = J3 = 0  # Initialize terms for J (end, even, odd)
    for i in range(0, n + 1):
        x = a + i * h  # Set x = a + i*h
        HX = (d(x) - c(x)) / m  # Calculate HX for y-interval
        K1 = f(x, c(x)) + f(x, d(x))  # End terms for y
        K2 = K3 = 0  # Initialize even and odd terms for y
        for j in range(1, m):
            y = c(x) + j * HX  # Set y = c(x) + j*HX
            Q = f(x, y)  # Evaluate f(x, y)
            if j % 2 == 0:
                K2 += Q
            else:
                K3 += Q
        L = (K1 + 2 * K2 + 4 * K3) * HX / 3
        if i == 0 or i == n:
            J1 += L
        elif i % 2 == 0:
            J2 += L
        else:
            J3 += L
    J = h * (J1 + 2 * J2 + 4 * J3) / 3
    return J
def f(x, y):
    return np.log(x + 2*y)  # Function to integrate
a = 1.4  # Lower limit for x
b = 2.0  # Upper limit for x
def c(x):
    return 1.0  # Lower limit for y as a function of x

def d(x):
    return 1.5  # Upper limit for y as a function of x
# Number of subintervals (must be even)
m = 2  # Subintervals in y
n = 4 # Subintervals in x
# Approximate the double integral
result = simpsons_double_integral(f, a, b, c, d, m, n)
print(f"Approximated value of the double integral: {result}")
