'''
Generate a list of 100 random integers between 1 and 100 and plot a histogram of the same.
'''
import random
import matplotlib.pyplot as plt

# Generate a list of 100 random integers between 1 and 100
random_integers = [random.randint(1, 100) for _ in range(100)]

# Plot a histogram
plt.hist(random_integers, bins=20, color='blue', alpha=0.5,edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 100 Random Integers between 1 and 100')
plt.grid(True)
plt.show()
