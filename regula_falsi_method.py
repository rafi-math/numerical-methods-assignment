import math

def regula_falsi(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return None

    while True:
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

fx = input("Enter f(x): ")
a = float(input("a: "))
b = float(input("b: "))
tol = float(input("tolerance: "))

def f(x):
    return eval(fx)

result = regula_falsi(a, b, tol)
if result is not None:
    print(round(result, 4))
