'''
Write a python program to randomly generate data with 100 numbers and form a histogram of it.
Range of numbers should be between 1 to 100(both included), bucket size=10.
'''
import random
import matplotlib.pyplot as plt

# Step 1: Generate random data
data = [random.randint(1, 100) for _ in range(100)]
print (data)

# Step 2: Create histogram data
# Define the number of bins and the range of each bin
bins = list(range(0, 101, 10))
print(bins)
# Step 3: Plot the histogram
plt.hist(data, bins=bins, edgecolor='black')

# Add titles and labels
plt.title('Histogram of Randomly Generated Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Display the histogram
plt.show()

'''
output

[18, 18, 42, 94, 10, 36, 18, 7, 24, 39, 53, 12, 62, 77, 17, 53, 72, 81, 80,
 41, 94, 23, 53, 2, 94, 70, 9, 9, 99, 19, 13, 64, 74, 74, 21, 21, 41, 56, 86,
 17, 16, 70, 34, 50, 75, 67, 64, 97, 92, 99, 56, 50, 13, 81, 36, 9, 64, 47, 34, 
 8, 94, 99, 69, 42, 41, 20, 21, 51, 55, 39, 51, 89, 63, 100, 63, 48, 16, 76, 
 95, 30, 70, 34, 100, 30, 90, 70, 92, 68, 92, 68, 89, 42, 35, 41, 38, 66, 
 8, 33, 39, 69]

[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''

'''
    Generating Random Data:
        random.randint(1, 100) generates a random integer between 1 and 100 (both inclusive).
        A list comprehension [random.randint(1, 100) for _ in range(100)]
        generates 100 such random integers.

    Creating Histogram Data:
        bins = list(range(0, 101, 10)) creates the bins for the histogram. 
        The range function generates numbers from 0 to 100 with a step size of 10.
        The 101 is used to ensure the upper limit of 100 is included in the last bin.

    Plotting the Histogram:
        plt.hist(data, bins=bins, edgecolor='black') plots the histogram with
        specified bins and edge color for better visibility of the bin edges.
        Titles and labels are added for clarity using plt.title, plt.xlabel, 
        and plt.ylabel.
        Finally, plt.show() displays the histogram.
'''