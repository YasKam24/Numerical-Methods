import numpy as np
# Newton Forwward Difference Interpolation
'''
Given function points
x = [ -0.75, -0.5, -0.25, 0]
y = [-0.07181250, -0.02475, -0.3349375, 1.101000]
we want to interpolate the value of  f(-1/3) using newton forward divided difference
'''
# Example usage:
x = np.array([-0.75, -0.5, -0.25, 0])
y = np.array([-0.07181250, -0.02475, 0.3349375, 1.101000])
def DividedDiff(x_values , y_values):
    n = len(x_values)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = diff_table[i + 1, j - 1] - diff_table[i, j - 1]
    return diff_table
def forward_difference_1(p, x, y):
    h = x[1] - x[0]
    s = (p - x[0]) / h
    return DividedDiff(x, y)[0, 0] + (s) * (y[1] - y[0])
def forward_difference_2(p, x, y):
    h = x[1] - x[0]
    s = (p - x[0]) / h
    return forward_difference_1(p, x, y) + ((s) * (s - 1)* DividedDiff(x, y)[0, 2]) / (2)
def forward_difference_3(p, x, y):
    h = x[1] - x[0]
    s = (p - x[0]) / h
    return forward_difference_2(p, x, y) + ((s) * (s - 1) * (s - 2) * DividedDiff(x, y)[0, 3]) / (6)
print(DividedDiff(x, y))
print(forward_difference_1(-1/3, x, y))
print(forward_difference_2(-1/3, x, y))
print(forward_difference_3(-1/3, x, y))
