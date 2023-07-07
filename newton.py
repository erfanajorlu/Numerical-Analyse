def answer(ne, i, x):
    ans = []

    for j in range(i):
        p = [-1 * x[j], 1]
        ans.append(p)

    for j in range(1, len(ans)):
        ans1 = multi(ans[0], ans[j])
        ans[0] = ans1

    if i == 0:
        return [ne[i]]
    else:
        for j in range(len(ans[0])):
            ans[0][j] = ans[0][j] * ne[i]
        return ans[0]


def calc(p, x):
    ans = 0
    for i in range(len(p)):
        ans += p[i] * (x ** i)
    return ans


def multi(A, B):
    s = len(A) + len(B) - 1
    ans = []
    for i in range(s):
        ans.append(0)
    for i in range(len(A)):
        for j in range(len(B)):
            ans[i+j] += A[i] * B[j]
    return ans


n = int(input("Enter n->"))
x = []
f = []
# get xi and fi
for i in range(n):
    x1 = float(input(f"Enter x{i} -> "))
    x.append(x1)
    x1 = float(input(f"Enter f{i} -> "))
    f.append(x1)
k = 1
ans = []
ans.append(f[0])

F = [[0]*n for i in range(n)]
for i in range(n):
    F[0][i] = f[i]

# do Newton’s Divided-Difference
while len(f) != 1:
    j = 0
    for i in range(n-1):
        if i+k >= n:
            break
        f[j] = (f[j] - f[j+1]) / (x[i] - x[i+k])
        F[k].append(round(f[j], 7))
        j += 1
    ans.append(f[0])
    f.pop()
    k += 1

ans1 = []

for i in range(n):
    ans1.append(answer(ans, i, x))

ans2 = []
for i in range(n):
    ans2.append(0)

for i in range(n):
    for j in range(len(ans1[i])):
        ans2[j] += ans1[i][j]

for i in range(n-1, 0, -1):
    print(f"({ans2[i]} x^{i})", end="+ ")

print(f"({ans2[0]} x^{0})")
calculate = True
while calculate:
    print("do you want to calculate any x?")
    s = int(input("""1-YES
2-No
"""))
    if s == 2:
        calculate = False
    else:
        m = float(input("enter your number ->"))
        ans1 = calc(ans2, m)
        print(ans1)
print("Good By")