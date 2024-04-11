'''
Using the Binomial(n, p) distribution plot a histogram to show the actual binomial samples. 
Use a line chart to show the normal approximation. 
Plot both in the same graph. 
Take n=100, p=0.75 and number of points should be 100.
'''
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters
n = 100
p = 0.75
num_points = 100

# Generate binomial samples
binomial_samples = binom.rvs(n, p, size=num_points)

# Generate x values for normal approximation
x_values = [i for i in range(n+1)]

# Calculate normal approximation
mu = n * p
sigma = (n * p * (1 - p)) ** 0.5
normal_approximation = [norm.pdf(x, loc=mu, scale=sigma) for x in x_values]

# Plot histogram of actual binomial samples
plt.hist(binomial_samples, bins=20, color='blue', alpha=0.5, label='Binomial Samples')

# Plot normal approximation
plt.plot(x_values, normal_approximation, color='red', label='Normal Approximation')

plt.title('Binomial Distribution and Normal Approximation')
plt.xlabel('Number of Successes')
plt.ylabel('Frequency / Probability Density')
plt.legend()
plt.grid(True)
plt.show()
