'''
What is curse of dimensionality? Write a python program to show it by calculating minimum distances
between points when dimensions increase.
'''

'''
The "curse of dimensionality" refers to various phenomena that arise when analyzing and 
organizing data in high-dimensional spaces that do not occur in low-dimensional settings. 
As the number of dimensions increases, the volume of the space increases exponentially,
 causing several issues such as:

    Sparsity: Data points become sparse, making it difficult to find meaningful patterns.
    Distance Metrics: Distances between points tend to become less informative. 
                        In high dimensions, the distance between any two points tends to converge to the same value.
    Computational Complexity: Algorithms that rely on distance metrics become computationally expensive.
'''
import numpy as np
import matplotlib.pyplot as plt

def min_distances(num_points, max_dims):
    min_dists = []

    for dim in range(1, max_dims + 1):
        points = np.random.rand(num_points, dim)
        dists = []
        for i in range(num_points):
            for j in range(i + 1, num_points):
                dist = np.linalg.norm(points[i] - points[j])
                dists.append(dist)
        min_dists.append(np.min(dists))

    return min_dists

num_points = 100
max_dims = 20

min_dists = min_distances(num_points, max_dims)

plt.plot(range(1, max_dims + 1), min_dists, marker='o')
plt.title('Minimum Distance between Points in Increasing Dimensions')
plt.xlabel('Number of Dimensions')
plt.ylabel('Minimum Distance')
plt.grid(True)
plt.show()


'''
output

graph


'''

'''
    Import Necessary Libraries:
        numpy for generating random points and calculating distances.
        matplotlib.pyplot for plotting the results.

    Define the Function min_distances:
        This function generates random points in increasing dimensions and calculates the minimum distance between any pair of points.
        num_points: Number of points to generate.
        max_dims: Maximum number of dimensions to consider.
        For each dimension, generate num_points random points.
        Calculate the Euclidean distance between every pair of points and find the minimum distance.

    Generate and Plot the Results:
        num_points = 100: Number of points to generate in each dimension.
        max_dims = 20: Maximum number of dimensions to consider.
        min_dists = min_distances(num_points, max_dims): Calculate the minimum distances.
        Plot the minimum distances as a function of the number of dimensions.
'''