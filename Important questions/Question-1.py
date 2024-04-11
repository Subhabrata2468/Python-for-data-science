# -*- coding: utf-8 -*-
"""
compute_covariance and compute_correlation
"""

def compute_mean(data):
    return sum(data) / len(data)

def compute_covariance(x, y):
    if len(x) != len(y):
        return "Length of datasets must be the same"
    else:
        mean_x = compute_mean(x)
        mean_y = compute_mean(y)
        covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))) / (len(x) - 1)
        return covariance

def compute_correlation(x, y):
    if len(x) != len(y):
        return "Length of datasets must be the same"
    else:
        covariance = compute_covariance(x, y)
        std_dev_x = (compute_covariance(x, x)) ** 0.5
        std_dev_y = (compute_covariance(y, y)) ** 0.5
        correlation = covariance / (std_dev_x * std_dev_y)
        return correlation

hours_movie = [10, 12, 14, 8]
hours_sleep = [40, 48, 56, 32]

covariance = compute_covariance(hours_movie, hours_sleep)
correlation = compute_correlation(hours_movie, hours_sleep)

print("Covariance between hours watching movies and hours sleeping:", covariance)
print("Correlation between hours watching movies and hours sleeping:", correlation)

'''
Covariance between hours watching movies and hours sleeping: 26.666666666666668
Correlation between hours watching movies and hours sleeping: 1.0000000000000002
'''