f = input("Enter dy/dx: ")

x = float(input("Initial x: "))
y = float(input("Initial y: "))
n = int(input("Number of steps: "))
h = float(input("Step size: "))

for i in range(1, n + 1):
    y = y + h * eval(f)
    x = x + h

print("Approximate value:", y)