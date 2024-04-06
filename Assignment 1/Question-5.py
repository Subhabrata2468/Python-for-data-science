'''
Use the following data to plot the number of applicants per year as a scatter plot. year = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
No. application per year = [921261, 929198, 1043739, 1186454, 1194938, 1304495, 1356805,
1282000, 479651]
'''
import matplotlib.pyplot as plt

# Data
year = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
no_of_applications = [921261, 929198, 1043739, 1186454, 1194938, 1304495, 1356805, 1282000, 479651]

# Create scatter plot
plt.scatter(year, no_of_applications, color='red')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of Applicants')
plt.title('Number of Applicants per Year')

# Display the plot
plt.show()
