# Secant mMethod

import numpy as np
import matplotlib.pyplot as plt


# Define the function
def f(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9

# Generate x values and corresponding y values
x_values = np.linspace(-2, 4, 400)
y_values = f(x_values)

# Plot the function
plt.plot(x_values, y_values, label='f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = 230x^4 + 18x^3 + 9x^2 - 221x - 9')
plt.legend()
plt.grid(True)
plt.show()


import sys
import os

def check_venv():
    venv_path = os.path.basename(sys.prefix)
    print(f"Python executable is at: {sys.executable}")
    if "venv" in venv_path or "env" in venv_path:
        print("Virtual environment is activated.")
    else:
        print("Virtual environment is NOT activated.")

check_venv()



def Secant(f, p0, p1):
    tol = 1e-4
    maxiter = 100
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i < maxiter:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        if abs(p - p1) < tol:
            return p, i
        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    return "No solution found"

def f(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9

print("Answer 4")
print(Secant(f, -1, 0))
print(Secant(f, 0, 1))

     