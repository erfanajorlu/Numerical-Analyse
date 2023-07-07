def f(x):
    return 2*x


def trapezoidal(a,b,h):
    n = int((b - a) // h)
    x = [a]
    k = a
    for i in range(n):
        k += h
        k = round(k , 4)
        x.append(k)
    y = []
    for i in x:
        y.append(f(i))
    ans = y[0] + y[len(y) - 1]
    for i in range(1,len(y) - 1):
        ans += 2 * y[i]
    ans = ans * (h / 2)
    ans = round(ans,4)
    return ans
 

a = float(input("enter a -> "))
b = float(input("enter b -> "))
h = float(input("enter h -> "))
print(trapezoidal(a,b,h))