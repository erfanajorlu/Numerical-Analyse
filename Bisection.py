def f(x):
    return x**3 - x - 1


def Bisection(a, b, Tol , iteration):
    for i in range(iteration):
        x = (a + b) / 2.0
        if abs(f(x)) < Tol:
            return x
        elif f(a) * f(x) > 0:
            a = x
        else:
            b = x
    return f"Maximum number of iterations exceeded."


a = float(input("enter a:"))
b = float(input("enter b:"))
Tol = float(input("enter Tol:"))
iteration = int(input("enter iteration:"))
if f(a) * f(b) > 0:
    print(f(a))
    print(f(b))
    print("The function must have opposite signs at the interval endpoints.")
else:
    print(Bisection(a ,b , Tol , iteration))
