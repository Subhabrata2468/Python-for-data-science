'''
Find the point of minima of Rosenbrock function using Gradient Descent method taking
initial solution (0,0). Rosenbrock function is defined below. f(x, y) = (1 − x) 2 + (y− x 2 ) 2 .
'''
import numpy as np

# Define the Rosenbrock function
def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

# Define the partial derivatives of the Rosenbrock function
def rosenbrock_grad(x, y):
    df_dx = -2 * (1 - x) - 400 * x * (y - x**2)
    df_dy = 200 * (y - x**2)
    return np.array([df_dx, df_dy])

# Gradient Descent method for Rosenbrock function
def gradient_descent(x0, y0, learning_rate, tolerance, max_iterations):
    point = np.array([x0, y0])
    for i in range(max_iterations):
        grad = rosenbrock_grad(point[0], point[1])
        new_point = point - learning_rate * grad
        if np.linalg.norm(new_point - point) < tolerance:
            print(f"Converged after {i+1} iterations")
            break
        point = new_point
    return point

# Initial solution
x0, y0 = 0, 0
# Learning rate
learning_rate = 0.001
# Tolerance for convergence
tolerance = 1e-6
# Maximum number of iterations
max_iterations = 100000

# Find the point of minima
minima = gradient_descent(x0, y0, learning_rate, tolerance, max_iterations)
print(f"The point of minima is at (x, y) = ({minima[0]}, {minima[1]})")
print(f"The value of the function at this point is f(x, y) = {rosenbrock(minima[0], minima[1])}")

'''
Converged after 14019 iterations
The point of minima is at (x, y) = (0.998883167548619, 0.9977631102939291)
The value of the function at this point is f(x, y) = 1.2493147084281799e-06
'''
