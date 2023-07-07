def f(x, y):
    return x + y


def euler(x0, y0, i, h):
    k = x0
    y = y0
    while k < i:
        y = y0 + (h * f(k, y0))
        y0 = y
        k += h
    y = round(y , 5)
    return y


y0 = 1
x0 = 0

i = float(input("enter i :"))
h = float(input("enter h :"))
print(euler(x0, y0, i, h))
