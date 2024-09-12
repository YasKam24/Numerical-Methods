import numpy as np

def gaussian_double_integral(f, a, b, c, d, r, c_mn, n, m):
    h1 = (b - a) / 2
    h2 = (b + a) / 2
    J = 0
    for i in range(m):
        JX = 0  # Initialize JX for each i
        x = h1 * r[i] + h2  # Step 3: Compute x value using Gaussian roots
        d1 = d(x)
        c1 = c(x)
        k1 = (d1 - c1) / 2
        k2 = (d1 + c1) / 2
        for j in range(n):
            y = k1 * r[j] + k2  # Compute y value
            Q = f(x, y)  # Evaluate f(x, y)
            JX += c_mn[j] * Q  # Update JX for this j
        J += c_mn[i] * k1 * JX
    J *= h1
    return J
def f(x, y):
    return np.log(x + 2 * y)  # Function to integrate
a = 1.4  # Lower limit for x
b = 2.0  # Upper limit for x
def c(x):
    return 1.0  # Lower limit for y as a function of x
def d(x):
    return 1.5  # Upper limit for y as a function of x
r = [-0.57735026919, 0.57735026919]  # Roots for n = 2 Gaussian quadrature
c_mn = [1.0, 1.0]  # Weights for 2-point Gaussian quadrature
n = 2  # Points in y (should match roots and coefficients length)
m = 2  # Points in x (should match roots and coefficients length)
result = gaussian_double_integral(f, a, b, c, d, r, c_mn, n, m)
print(f"Approximated value of the double integral: {result}")

