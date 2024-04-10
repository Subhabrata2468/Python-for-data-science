'''
Plot a bar chart with axis labels for given data:
mentions = [500, 505]
years = [2017, 2018]
Do not give any extra condition for x-axis as well as y-axis.
 Now again plot the bar chart for this data and start y-axis from 0.
State the difference in both the bar chart.
'''
import matplotlib.pyplot as plt

# Data
mentions = [500, 505]
years = [2017, 2018]

# Create bar chart with y-axis starting from 0
plt.bar(years, mentions)

# Set y-axis limits
plt.ylim(0, max(mentions) + 100)  # Add some padding for better visualization

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Mentions')
plt.title('Mentions Over Years')

# Show the plot
plt.show()
