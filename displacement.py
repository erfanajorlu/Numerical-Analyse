#روش نابجایی
def f(x):
    return x**3 - x - 1


def displacement(a, b, Tol, iteration):
    for i in range(iteration):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(x)) < Tol:
            return x
        elif f(a) * f(x) > 0:
            a = x
        else:
            b = x


a = float(input("enter a:"))
b = float(input("enter b:"))
Tol = float(input("enter Tol:"))
iteration = int(input("enter iteration:"))
if f(a) * f(b) > 0:
    print(f(a))
    print(f(b))
    print("The function must have opposite signs at the interval endpoints.")
else:
    print(displacement(a, b, Tol, iteration))