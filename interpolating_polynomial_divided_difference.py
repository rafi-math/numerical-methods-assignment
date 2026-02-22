import sympy as sp

def newton_divided(x, f, value):
    n = len(f)
    d = [f[:]]

    for i in range(1, n):
        row = []
        for j in range(n - i):
            row.append((d[i-1][j+1] - d[i-1][j]) / (x[j+i] - x[j]))
        d.append(row)

    X = sp.symbols('x')
    poly = d[0][0]
    term = 1

    for i in range(1, n):
        term *= (X - x[i-1])
        poly += d[i][0] * term

    poly = sp.expand(poly)
    val = poly.subs(X, value)

    return poly, val


x = list(map(float, input("Enter x values: ").split()))
f = list(map(float, input("Enter f(x) values: ").split()))
value = float(input("Enter value to find: "))

p, val = newton_divided(x, f, value)

print("Polynomial =", p)
print("Value =", float(val))