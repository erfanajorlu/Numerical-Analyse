# Erfan Ajorlu
n = int(input("Enter n->"))
X = []
f = []
x = float(input("Enter X => "))
for i in range(n):
    x1 = float(input(f"Enter x{i} ->"))
    X.append(x1)
    x1 = float(input(f"Enter f{i} ->"))
    f.append(x1)

Q = [[0]*n for i in range(n)]

for i in range(n):
    Q[0][i] = f[i]

for i in range(1, n):
    for j in range(1, i+1):
        Q[j][i] = (((x - X[i-j])*Q[j-1][i]) - ((x - X[i])
                   * Q[j-1][i-1])) / (X[i] - X[i-j])
        Q[j][i] = round(Q[j][i], 6)

for i in range(n):
    print(*Q[i])
