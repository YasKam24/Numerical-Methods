#False_Position

def false(f, p0, p1):
    tol = 1e-6
    maxiter = 100
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i < maxiter:
        p = p1 - q1 * (p0 - p1)/(q0 - q1)
        if abs(p - p1) < tol:
            return p, i
        i += 1
        q = f(p)
        if q * q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    return "No solution found"

def f(x):   
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9

print("Answer 4")
print(false(f, -1, 0))
print(false(f, 0, 1))