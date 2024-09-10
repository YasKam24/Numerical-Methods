# Bisection Method

def f(x):
    return x**3 - 7*(x**2) + 14*x - 6

def Bisection(a, b, f):
    tol = 1e-4
    maxiter = 1000
    i = 1
    while i < maxiter or (b - a) < tol:
        p = a + (b - a)/2
        if f(p) == 0 or (b - a)/2 < tol: 
            return p, i
        if f(a)*f(p) > 0:
            a = p
        else:
            b = p
        i += 1
    return "No solution found"

print("Answer 1")
print("Part 1", Bisection(0, 1, f))
print("Part 2", Bisection(1, 3.2, f))
print("Part 3", Bisection(3.2, 4, f))