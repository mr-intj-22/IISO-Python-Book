'''
This is to plot the 3rd order polynomial in Section 1.3
'''

import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function
def polynomial(x):
    return 2 * x**3 - 3 * x**2 + x - 5

# Given x values
x_values = np.array([-2, -1, 0, 1, 2])

# Calculate y values based on the polynomial
y_values = polynomial(x_values)

# Generate a range of x values for a smooth curve
x_curve = np.linspace(-3, 3, 400)
y_curve = polynomial(x_curve)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_curve, y_curve, label='Polynomial: $2x^3 - 3x^2 + x - 5$', color='blue')
plt.scatter(x_values, y_values, color='red', zorder=5, label='Given Points')
plt.title('Plot of the Polynomial and Given Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()