# روش وتری
def f(x):
    return x**3 - x - 1


def secant(x0, x1, tol, max_iter):
    x = x1
    xn = x0
    iter_count = 0
    while iter_count < max_iter:
        iter_count += 1
        if abs(f(x) - f(xn)) < tol:
            return ("Division by zero encountered")
            
        x_new = x - (f(x) * (x - xn) / (f(x) - f(xn)))
        if abs(x_new - x) < tol and abs(f(x_new)) < tol:
            return x_new
        xn = x
        x = x_new


x0 = float(input("enter x0:"))
x1 = float(input("enter x1:"))
Tol = float(input("enter Tol:"))
iteration = int(input("enter iteration:"))
print(secant(x0, x1, Tol, iteration))
