'''
Find the gradient of Rosenbrock function using limit of the difference coefficient method
at the point (1,2). Rosenbrock function is defined below. f(x,y) = (1 − x) 2 + 100(y − x 2 ) 2
'''
def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

def partial_derivative_x( x, y, h):
    return (f(x + h, y) - f(x, y)) / h

def partial_derivative_y(x, y, h):
    return (f(x, y + h) - f(x, y)) / h

x = 1
y = 2
h = 0.000001

# Calculate the partial derivatives at (x, y)
partial_x = partial_derivative_x(x, y, h)
partial_y = partial_derivative_y(x, y, h)

print(f"The partial derivative with respect to x at (1, 2) is approximately {partial_x}")
print(f"The partial derivative with respect to y at (1, 2) is approximately {partial_y}")

# Gradient at (1, 2)
gradient = (partial_x, partial_y)
print(f"The gradient of the Rosenbrock function at (1, 2) is approximately {gradient}")

'''
The partial derivative with respect to x at (1, 2) is approximately -399.9997989865278
The partial derivative with respect to y at (1, 2) is approximately 200.00010003684565
The gradient of the Rosenbrock function at (1, 2) is approximately (-399.9997989865278, 200.00010003684565)
'''
