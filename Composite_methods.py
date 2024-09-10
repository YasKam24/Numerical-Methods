import math


#composite methods
def composite_rectangular_method(f, a, b, n):
    intervals = []
    h = (b - a) / n
    for i in range(n):
        intervals.append([a + i*h, a + (i + 1)*h])
    sum = 0
    for i in intervals:
        sum += f(i[0]) * (i[1] - i[0])
    return sum

def composite_midpoint_method(f, a, b, n):
    intervals = []
    h = (b - a) / n
    for i in range(n):
        intervals.append([a + i*h, a + (i+1)*h])
    sum =0
    for i in intervals:
        sum += f((i[0]+i[1])/2)
    return sum * h

def composite_trapezoidal_method(f, a ,b, n):
    intervals = []
    h = (b - a)/n
    for i in range(n):
        if i ==0 or i == n:
            intervals.append(f(a + i*h))
        else:
            intervals.append(2*f(a+i*h))
    return (h/2) * sum(intervals)

def composite_simpsons_method(f, a, b, n):
    h = (b - a)/n
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += 2*(f(a + i*h))
        else:
            sum += 4*(f(a + i*h))
    return (h/3) * (sum + f(a) + f(b))

print(composite_rectangular_method(lambda x: (x**3)*math.exp(x), -2, 2, 4))
print(composite_midpoint_method(lambda x: (x**3)*math.exp(x), -2, 2, 4))
print(composite_trapezoidal_method(lambda x: (x**3)*math.exp(x), -2, 2, 4))
print(composite_simpsons_method(lambda x: (x**3)*math.exp(x), -2, 2, 4))
print(composite_rectangular_method(lambda x: math.tan(x), 0, 3*math.pi/8, 8))
print(composite_midpoint_method(lambda x: math.tan(x), 0, 3*math.pi/8, 8))
print(composite_trapezoidal_method(lambda x: math.tan(x), 0, 3*math.pi/8, 8))
print(composite_simpsons_method(lambda x: math.tan(x), 0, 3*math.pi/8, 8))


