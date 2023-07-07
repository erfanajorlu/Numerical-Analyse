def jakubi(A , b , x0 , iteration , n):
    ans = x0[::]
    k = 1
    while k <= iteration:
        k += 1
        ans1 = [0 for i in range(n)]
        for i in range(n):
            ans1[i] += b[i]
            for j in range(n):
                if j != i:
                    ans1[i] += (-1) * (A[j][i] * ans[j])
            ans1[i] /= A[i][i]
        
        for i in range(n):
            ans[i] = round(ans1[i] , 4)
    return ans

n = int(input("enter n -> "))
iteration = int(input("enter iteration -> "))
x = []
for i in range(n):
    x1 = list(map(int , input(f"enter Coefficients for x{i} -> ").split()))
    x.append(x1)
b = list(map(int , input("enter matrix b ->").split()))
x0 = list(map(int , input("enter matrix x0 ->").split()))
print(jakubi(x , b , x0 , iteration , n))