# lagrange Interpolation

def lagrange_interpoaltion(n, x, y, val):
    result = 0
    for i in range(n):
        temp = 1
        for j in range(n):
            if i != j:
                temp *= (val - x[j])/(x[i] - x[j])
        result += temp*y[i]
    return result

x = [-0.75, -0.5, -0.25, 0]
y = [-0.07181250, -0.02475, 0.3349375, 1.101000]
print(f"When degree is 1 {lagrange_interpoaltion(1, x, y, -1/3)}")
print(f"When degree is 2 {lagrange_interpoaltion(2, x, y, -1/3)}")
print(f"When degree is 3 {lagrange_interpoaltion(3, x, y, -1/3)}")
print(f"When degree is 4 {lagrange_interpoaltion(4, x, y, -1/3)}")
