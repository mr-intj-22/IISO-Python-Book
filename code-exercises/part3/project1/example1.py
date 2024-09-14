'''
This is to plot the 3rd order polynomial in Section 1.3
'''

import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function
def polynomial(x, order):
    y = 0
    for i in range(order+1):
        y += i * x**i
    return y

x = np.linspace(-10, 10, 10, endpoint=True)

# Create the plot
fig, ax = plt.subplots(3,3)
ax[0,0].plot(x, [polynomial(xx, 0) for xx in x], '-ob')
ax[0,0].set_title("0th order polinomyal")
ax[0,0].grid(True)
ax[0,1].plot(x, [polynomial(xx, 1) for xx in x], '-ob')
ax[0,1].set_title("1sr order polinomyal")
ax[0,1].grid(True)
ax[0,2].plot(x, [polynomial(xx, 2) for xx in x], '-ob')
ax[0,2].set_title("2nd order polinomyal")
ax[0,2].grid(True)
ax[1,0].plot(x, [polynomial(xx, 3) for xx in x], '-ob')
ax[1,0].set_title("3rd order polinomyal")
ax[1,0].grid(True)
ax[1,1].plot(x, [polynomial(xx, 4) for xx in x], '-ob')
ax[1,1].set_title("4th order polinomyal")
ax[1,1].grid(True)
ax[1,2].plot(x, [polynomial(xx, 5) for xx in x], '-ob')
ax[1,2].set_title("5th order polinomyal")
ax[1,2].grid(True)
ax[2,0].plot(x, [polynomial(xx, 6) for xx in x], '-ob')
ax[2,0].set_title("6th order polinomyal")
ax[2,0].grid(True)
ax[2,1].plot(x, [polynomial(xx, 7) for xx in x], '-ob')
ax[2,1].set_title("7th order polinomyal")
ax[2,1].grid(True)
ax[2,2].plot(x, [polynomial(xx, 8) for xx in x], '-ob')
ax[2,2].set_title("8th order polinomyal")
ax[2,2].grid(True)
plt.suptitle("Degrees of Polynomials")
plt.tight_layout()
plt.show()