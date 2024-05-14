'''
Define p-value and find the two-sided p-value with and without continuity correction
when the values of x(observed no. of heads), mean and standard deviation are 110, 100, 5
respectively

'''

'''
Definition of p-value

A p-value is the probability of obtaining an observed result (or one more extreme) assuming 
that the null hypothesis is true. It helps us determine the statistical 
significance of the observed result. In the context of hypothesis testing, 
a low p-value (typically less than 0.05) indicates that the observed data is 
unlikely under the null hypothesis, and thus, we may reject the null hypothesis.
'''
import scipy.stats as stats

# Given values
x_observed = 110
mean = 100
std_dev = 5

# Calculate z-score without continuity correction
z = (x_observed - mean) / std_dev

# Calculate the one-sided p-value without continuity correction
p_value_one_sided = 1 - stats.norm.cdf(z)

# Calculate the two-sided p-value without continuity correction
p_value_two_sided = 2 * p_value_one_sided

print(f"Two-sided p-value without continuity correction: {p_value_two_sided:.4f}")

# Apply continuity correction
x_corrected = 109.5

# Calculate z-score with continuity correction
z_corrected = (x_corrected - mean) / std_dev

# Calculate the one-sided p-value with continuity correction
p_value_one_sided_corrected = 1 - stats.norm.cdf(z_corrected)

# Calculate the two-sided p-value with continuity correction
p_value_two_sided_corrected = 2 * p_value_one_sided_corrected

print(f"Two-sided p-value with continuity correction: {p_value_two_sided_corrected:.4f}")


'''
Two-sided p-value without continuity correction: 0.0455
Two-sided p-value with continuity correction: 0.0574
'''