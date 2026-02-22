n = int(input("Enter number of variables: "))

a = []

for i in range(1, n+1):
    print("Enter coefficients and constant for equation", i)
    row = list(map(float, input().split()))
    a.append(row)

for i in range(n):
    pivot = a[i][i]
    for j in range(n+1):
        a[i][j] /= pivot

    for k in range(n):
        if k != i:
            factor = a[k][i]
            for j in range(n+1):
                a[k][j] -= factor * a[i][j]

print("Solution:")
for i in range(n):
    print("x"+str(i+1), "=", round(a[i][n], 6))