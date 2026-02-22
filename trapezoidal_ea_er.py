import math
import sympy as sp

fx = input("Enter f(x): ")
a = float(input("a: "))
b = float(input("b: "))
n = int(input("Number of subintervals: "))

x = sp.symbols('x')
f_sym = sp.sympify(fx)
f_num = sp.lambdify(x, f_sym, "math")

h = (b - a) / n

T = f_num(a) + f_num(b)

for i in range(1, n):
    T += 2 * f_num(a + i * h)

T = (h / 2) * T

exact_value = float(sp.integrate(f_sym, (x, a, b)))

absolute_error = abs(exact_value - T)

if abs(exact_value) < 1e-12:
    relative_error = "Undefined"
else:
    relative_error = absolute_error / abs(exact_value)

print("Trapezoidal Approximation:", T)
print("Exact Value:", exact_value)
print("Absolute Error:", absolute_error)
print("Relative Error:", relative_error)