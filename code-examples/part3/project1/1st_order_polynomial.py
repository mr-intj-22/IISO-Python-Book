import matplotlib.pyplot as plt

def first_order_polynomial(X: list[int], a: float, b: float) -> list[float]:

    Y: list[float] = []
    for x in X:
        y = a * x + b
        Y.append(y)

    return Y


x = list(range(-10, 10))
y = first_order_polynomial(x, 2, -2)

plt.plot(x, y, "-o", label="Line")
plt.title("First Order Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
