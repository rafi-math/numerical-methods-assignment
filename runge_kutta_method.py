f = input("Enter dy/dx: ")

x = float(input("Initial x: "))
y = float(input("Initial y: "))
n = int(input("Number of steps: "))
h = float(input("Step size: "))

for i in range(1, n + 1):
    k1 = h * eval(f)
    k2 = h * eval(f.replace("x", f"({x + h / 2})").replace("y", f"({y + k1 / 2})"))
    k3 = h * eval(f.replace("x", f"({x + h / 2})").replace("y", f"({y + k2 / 2})"))
    k4 = h * eval(f.replace("x", f"({x + h})").replace("y", f"({y + k3})"))

    y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    x = x + h

print("Approximate value:", y)