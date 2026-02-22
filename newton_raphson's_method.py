def newton_raphson(x, tol):
    count = 0
    while True:
        if df(x) == 0:
            print("Derivative is zero")
            return None

        x1 = x - f(x) / df(x)
        if abs(x1 - x) < tol:
            return x1

        x = x1
        count += 1
        if count > 1000:
            print("Did not converge")
            return None


fx = input("Enter f(x): ")
dfx = input("Enter f'(x): ")
x = float(input("Initial guess: "))
tol = float(input("tolerance: "))

def f(x):
    return eval(fx)

def df(x):
    return eval(dfx)

result = newton_raphson(x, tol)
if result is not None:
    print(round(result, 4))