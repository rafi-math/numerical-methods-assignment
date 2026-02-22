def newton_forward(x, f, value):
    n = len(f)
    diff = [f[:]]
    for i in range(1, n):
        row = []
        for j in range(n - i):
            row.append(diff[i-1][j+1] - diff[i-1][j])
        diff.append(row)

    h = x[1] - x[0]
    u = (value - x[0]) / h

    result = f[0]
    fact = 1
    u_term = 1

    for i in range(1, n):
        u_term = u_term * (u - (i - 1))
        fact = fact * i
        result = result + (u_term / fact) * diff[i][0]

    return result


x = list(map(float, input("Enter x values: ").split()))
f = list(map(float, input("Enter f(x) values: ").split()))
value = float(input("Enter value to find: "))

print(round(newton_forward(x, f, value), 6))