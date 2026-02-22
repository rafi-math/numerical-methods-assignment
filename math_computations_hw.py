import math
from sympy import symbols, integrate, sin, pi

x = 125
y = 5
z = math.sqrt(x - y**2) / (1 + (1 / (y - 2)) + math.sqrt(x))
print(z)

x_sym = symbols('x')
f = sin(x_sym)
result = integrate(f, (x_sym, 0, pi))
print(result)

x_val = 2
y_poly = x_val**3 + 3*x_val - 5
print(y_poly)

vt = 2/3
va = 0.67

ea = abs(vt - va)
er = abs(vt - va) / vt
ep = er * 100

print(ea)
print(er)
print(ep)