'''
Let X be a binomial random variable with parameters n = 100 and p = 0.6. Find the
approximate probability that: 1. X lies above 60. 2. X lies between 50 and 70. using normal
approximation to binomial distribution.
'''

import scipy.stats as stats
import math

# Parameters for the binomial distribution
n = 100
p = 0.6

# Mean and standard deviation for the binomial distribution
# 
mu = n * p
sigma = math.sqrt(n * p * (1 - p))

# 1. Probability that X lies above 60
# Apply continuity correction: X > 60 becomes X >= 61
x1 = 61
z1 = (x1 - mu) / sigma
prob_above_60 = 1 - stats.norm.cdf(z1)

# 2. Probability that X lies between 50 and 70
# Apply continuity correction: 50 <= X <= 70 becomes 49.5 < X < 70.5
x2_lower = 49.5
x2_upper = 70.5
z2_lower = (x2_lower - mu) / sigma
z2_upper = (x2_upper - mu) / sigma
prob_between_50_and_70 = stats.norm.cdf(z2_upper) - stats.norm.cdf(z2_lower)

# Output the results
print(f"Approximate probability that X lies above 60: {prob_above_60:.4f}")
print(f"Approximate probability that X lies between 50 and 70: {prob_between_50_and_70:.4f}")

'''
Approximate probability that X lies above 60: 0.4191
Approximate probability that X lies between 50 and 70: 0.9679
'''