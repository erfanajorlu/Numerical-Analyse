x = list(map(float, input("enter x:").split()))
f = list(map(float, input("enter f:").split()))
df = list(map(float, input("enter df:").split()))
n =len(x)
z = []
q = []
for i in range(2 * n):
    z.append(0)
    q.append([0 for i in range(2 * n)])
print(len(q))

for i in range(n):
    print(i)
    z[2 * i] = x[i]
    z[(2 * i) + 1] = x[i]
    q[2*i][0] = f[i]
    q[(2*i) + 1][0] = f[i]
    q[(2*i) + 1][1] = df[i]
    if i != 0:
        q[2*i][1] = (q[2*i][0] - q[2*i - 1][0]) / (z[2*i] - z[2*i - 1])
for i in range(2,2*n):
    for j in range(2, i + 1):
        q[i][j] = (q[i][j-1] - q[i-1][j-1]) / (z[i] - z[i-j])

for i in range(2 * n):
    print(q[i][i])
