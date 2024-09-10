import numpy as np
# Newton Forwward Difference Interpolation
'''
Given function points
x = [ -0.75, -0.5, -0.25, 0]
y = [-0.07181250, -0.02475, 0.3349375, 1.101000]
we want to interpolate the value of  f(-1/3) using newton backward divided difference
'''

import numpy as np

def DividedDiff(x, y):
    n = len(x)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for i in range(1, n):  
        for j in range(n - i):
            coef[j, i] = (coef[j + 1, i - 1] - coef[j, i - 1]) 
    return coef

def backward_difference_1(p, x, y):
    n = len(x)
    h = x[1] - x[0]
    s = (p - x[n - 1]) / h
    coef = DividedDiff(x, y)
    return coef[n - 1, 0] + s * coef[n - 2, 1] 

def backward_difference_2(p, x, y):
    n = len(x)
    h = x[1] - x[0]
    s = (p - x[n - 1]) / h
    coef = DividedDiff(x, y)
    return backward_difference_1(p, x, y) + (s * (s + 1)) * coef[n - 3, 2] * (1/2)

def backward_difference_3(p, x, y):
    n = len(x)
    h = x[1] - x[0]
    s = (p - x[n - 1]) / h
    coef = DividedDiff(x, y)
    return backward_difference_2(p, x, y) + (s * (s + 1) * (s + 2)) * coef[n - 4, 3] * ( 1 / 6)

# Example usage:
x = np.array([-0.75, -0.5, -0.25, 0])
y = np.array([-0.07181250, -0.02475, 0.3349375, 1.101000])

print(DividedDiff(x, y))

print(backward_difference_1(-1/3, x, y))

print(backward_difference_2(-1/3, x, y))

print(backward_difference_3(-1/3, x, y))
