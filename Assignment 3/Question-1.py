'''
Find the derivate of using limit of the difference coefficient method at x = 1.
f(x) = ex 2 + sin(x) − tan(x) + log(x)
'''
import math

x = 1
h = 0.000001
def f(x):
    return math.exp(x**2) + math.sin(x) - math.tan(x) + math.log(x)

def derivative(x, h):
    return (f(x + h) - f(x)) / h


# Calculate the derivative at x = 1
deriv = derivative(x, h)

print(f"The derivative of f(x) at x = {x} is approximately {deriv}")

'''
The derivative of f(x) at x = 1 is approximately 3.551349041952534
'''
