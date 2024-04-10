'''
Plot xsinx, x2sinx , x3sinx and x4sinx in a single plot in the range x ∈ [-10, 10].
'''

import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate y values for each function
y1 = x * np.sin(x)
y2 = x**2 * np.sin(x)
y3 = x**3 * np.sin(x)
y4 = x**4 * np.sin(x)

# Plot the functions
plt.plot(x, y1, label='x * sin(x)'  ) 
plt.plot(x, y2, label='x^2 * sin(x)')
plt.plot(x, y3, label='x^3 * sin(x)')
plt.plot(x, y4, label='x^4 * sin(x)')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of x*sin(x), x^2*sin(x), x^3*sin(x), x^4*sin(x)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
