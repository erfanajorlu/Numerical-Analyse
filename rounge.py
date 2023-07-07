def f(x, y):
    return x + y


def rounge(x0, y0, i, h):
    y = y0
    k = x0
    while k < i:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, k3 + y0)
        y = y0 + (1 / 6)*(k1 + 2 * k2 + 2*k3 + k4)
        y0 = y
        k += h
    return y


y0 = 1
x0 = 0

i = float(input("enter i :"))
h = float(input("enter h :"))
print(rounge(x0, y0, i, h))
