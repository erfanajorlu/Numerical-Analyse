def f(x):
    return x**3 - x - 1
def df(x):
    return 3*x**2 - 1
 
def newton_raphson( x0, tol, max_iter):
    x = x0
    iter_count = 0

    while iter_count < max_iter:
        iter_count += 1
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol or abs(f(x_new)) < tol:
            break
        x = x_new

    return x

x0 = float(input("enter x0:"))
Tol = float(input("enter Tol:"))
iteration = int(input("enter iteration:"))
print(newton_raphson(x0,Tol , iteration))