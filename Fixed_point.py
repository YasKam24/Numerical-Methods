# Fixed Point Iteration

def Fixed_point_iteration(g, x0):
    tol = 1e-10
    maxiter = 1000
    i = 0
    while i < maxiter:
        x = g(x0)
        if abs(x - x0) < tol:
            return x, i
        x0 = x
        i += 1
    return "No solution found"

def g(x):
    return ((3*x**2 + 3))**0.25

print("\nAnswer 2")
print(Fixed_point_iteration(g, 1)) 