'''
Plot histogram for age of male and female in different plots for the following data of male and female age.
male age = [53,51,71,31,33,39,52,27,54,30,64,26,21,54,52,20,59,32]
female age = [53,65,68,21,75,46,24,63,61,24,49,41,39,40,25,54,42,32,48,23,23]
'''

import matplotlib.pyplot as plt

# Data
male_age = [53, 51, 71, 31, 33, 39, 52, 27, 54, 30, 64, 26, 21, 54, 52, 20, 59, 32,45,49,45]
female_age = [53, 65, 68, 21, 75, 46, 24, 63, 61, 24, 49, 41, 39, 40, 25, 54, 42, 32, 48, 23, 23]

# Create separate plots for male and female ages
plt.figure(figsize=(12, 6))

# Male Age Histogram
plt.subplot(1, 2, 1)
plt.hist(male_age, bins=10, color='blue', alpha=0.7,edgecolor="black")
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Male Age Distribution')

# Female Age Histogram
plt.subplot(1, 2, 2)
plt.hist(female_age, bins=10, color='red', alpha=0.7,edgecolor="black")
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Female Age Distribution')


# Show the plots
plt.show()
