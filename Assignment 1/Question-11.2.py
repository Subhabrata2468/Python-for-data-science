'''Plot the scatter plot for following data with equal axis. Also State the difference in two.
test 1 grades = [ 99, 90, 85, 97, 80]
test 2 grades = [100, 85, 60, 90, 70] 
'''


#equal axis

import matplotlib.pyplot as plt

# Data
test1_grades = [99, 90, 85, 97, 80]
test2_grades = [100, 85, 60, 90, 70]

# Create scatter plot with equal axes
plt.scatter(test1_grades, test2_grades)


# Add labels and title
plt.xlabel('Test 1 Grades')
plt.ylabel('Test 2 Grades')
plt.axis("equal")
# Show the plot
plt.show()


