import numpy as np

n = int(input("Enter number of variables: "))

A = []
b = []

for i in range(n):
    row = list(map(float, input("Enter coefficients and constant: ").split()))
    A.append(row[:-1])
    b.append(row[-1])

A = np.array(A)
b = np.array(b)

x = np.linalg.solve(A, b)

for i in range(n):
    print("x"+str(i+1), "=", round(x[i], 6))