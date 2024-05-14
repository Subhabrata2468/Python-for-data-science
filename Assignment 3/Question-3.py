'''
 Find the point of minima of function using Gradient Descent method taking initial
solution x0 = 2. f(x) = x 2 + sin(x).
'''

import numpy as np

# Define the function f(x) = x^2 + sin(x)
def f(x):
    return x**2 + np.sin(x)

# Define the derivative of the function f'(x) = 2x + cos(x)
def f_prime(x):
    return 2*x + np.cos(x)

# Gradient Descent method
def gradient_descent(x0, learning_rate, tolerance, max_iterations):
    x = x0
    for i in range(max_iterations):
        grad = f_prime(x)
        new_x = x - learning_rate * grad
        if abs(new_x - x) < tolerance:
            print(f"Converged after {i+1} iterations")
            break
        x = new_x
    return x

# Initial solution
x0 = 2
# Learning rate
learning_rate = 0.1
# Tolerance for convergence
tolerance = 1e-6
# Maximum number of iterations
max_iterations = 1000

# Find the point of minima
minima = gradient_descent(x0, learning_rate, tolerance, max_iterations)
print(f"The point of minima is at x = {minima}")
print(f"The value of the function at this point is f(x) = {f(minima)}")

'''
Converged after 52 iterations
The point of minima is at x = -0.45018008157897416
The value of the function at this point is f(x) = -0.23246557514304614
'''