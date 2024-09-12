import math

def newtonIteration(p0, tol, N0):
    i = 0
    terms = []

    while (i < N0):

        p = p0 - f(p0)/f1(p0)
        terms.append(p0)

        if abs(p-p0) < tol:
            terms.append(p)
            return terms
            break
        i += 1
        p0 = p
    return None

def finalNewtonIteration(p0, tol, N0):
    i = 0
    terms = []

    while (i < N0):
        p = p0 - (f(p0)*f1(p0))/((f1(p0))*2 - f(p0)*f2(p0))
        terms.append(p0)
        if abs(p-p0) < tol:
            terms.append(p)
            return terms
            break
        i += 1
        p0 = p
    return None

def f(x):
    return math.e**x - x - 1

def f1(x):
    return math.e**x - 1
def f2(x):
    return math.e**x
first = newtonIteration(1, 1e-3, 11)
pi = math.log(first[-1]/first[-2])/math.log(first[-2]/first[-3])
for index, item in enumerate(first):
    print("Term No.", index+1, ":", item)
def f0(x):
    return math.e**x - x - 1
def f1(x):
    return math.e**x - 1
def f2(x):
    return math.e**x
def newton_method_list(x:int ,tol:int)->int:
    count=1
    error=[]
    while abs(f0(x)) > tol:
        temp=x
        count+=1
        x = x - f0(x)/f1(x)
        error.append(abs(x-temp))
    p = abs(math.log(error[-1]/error[-2])/math.log(error[-2]/error[-3]))
    return f"rate: {p}"

print(newton_method_list(0.6,10**-47))
