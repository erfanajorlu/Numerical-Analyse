def f(x):
    return 2 * x


def simpson(a, b, h):
    n = (b - a) // h
    if n % 2 != 0:
        return "n must be even"
    x = [a]
    k = a
    while k + h <= b:
        k += h
        k = round(k, 4)
        x.append(k)
    y = []
    for i in x:
        y.append(f(i))
    ans = y[0] + y[len(y) - 1]
    for i in range(1, len(y) - 1):
        if i % 2 == 1 :
            ans += 4 * y[i]
        else:
            ans += 2 * y[i]
    ans = (h / 3) * ans
    ans = round(ans, 4)
    return ans


a = float(input("enter a -> "))
b = float(input("enter b -> "))
h = float(input("enter h -> "))
print(simpson(a, b, h))
