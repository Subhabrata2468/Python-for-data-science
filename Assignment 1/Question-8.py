'''
Plot the temperature extremes in certain region of India for each month, starting in January,
which are given by (in degrees Celsius).
max: 17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18
min: -62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58
'''

import matplotlib.pyplot as plt

# Define the months
months = list(range(1, 13))

# Define the maximum and minimum temperatures
max_temperatures = [17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
min_temperatures = [-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(months, max_temperatures, color="red", label='Max Temperature (°C)')
plt.plot(months, min_temperatures, color="blue", label='Min Temperature (°C)')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Extremes in a Certain Region of India')
plt.xticks(months)
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
