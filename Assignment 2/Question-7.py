'''
We have defined the function normal cdf. Write a program to invert normal cdf to find the value corresponding to a specified probability
'''
import math

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / (sigma * math.sqrt(2)))) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    # If the probability is 0 or 1, return the corresponding value
    if p <= 0:
        return -math.inf
    elif p >= 1:
        return math.inf
    
    # Use binary search to find the inverse
    low_z, low_p = -10.0, 0
    high_z, high_p = 10.0, 1
    while high_z - low_z > tolerance:
        mid_z = (low_z + high_z) / 2
        mid_p = normal_cdf(mid_z, mu, sigma)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            high_z, high_p = mid_z, mid_p
        else:
            break
    
    return mid_z

# Example usage:
probability = 0.6
value = inverse_normal_cdf(probability)
print(f"The value corresponding to a probability of {probability} is approximately {value:.4f}.")

'''
The value corresponding to a probability of 0.6 is approximately 0.2533.
'''
