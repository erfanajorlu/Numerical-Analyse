import math
def f(x):
    return x ** 5


def trapezoidal(a, b, n):
    h = (b - a) / n
    x = [a]
    k = a
    for i in range(n):
        k += h
        k = round(k, 2)
        x.append(k)
    y = []
    for i in x:
        y.append(f(i))
    ans = y[0] + y[len(y) - 1]
    for i in range(1, len(y) - 1):
        ans += 2 * y[i]
    ans = ans * (h / 2)
    ans = round(ans, 4)
    return ans


def romberg(a, b, n):
    RArray = [[0] * (n-i) for i in range(n)] 
    for i in range(n):
        RArray[0][i] = trapezoidal(a, b, i+1)
    for k in range(1,n):
        for j in range(1,n-k+1):
            RArray[k][j-1] = RArray[k-1][j] + ((RArray[k-1][j]-RArray[k-1][j-1])/(4**(k)-1))
    return RArray[n-1]


a = float(input("enter a -> "))
b = float(input("enter b -> "))
n = int(input("enter n -> "))
print(romberg(a, b, n))
