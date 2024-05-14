'''
Find the derivate of using limit of the difference coeffficient method at x = 1.
f(x) = ex 2 + sin(x) − tan(x) + log(x)
'''
import math

x = 1
h = 0.000001
def f(x):
    return math.exp(x**2) + math.sin(x) - math.tan(x) + math.log(x)

def derivative(f, x, h):
    return (f(x + h) - f(x)) / h


# Calculate the derivative at x = 1
deriv = derivative(f, x, h)

print(f"The derivative of f(x) at x = {x} is approximately {deriv}")
