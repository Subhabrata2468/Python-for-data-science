'''
Write a function to compute the component-wise mean of a list of vectors. Assert the condition that the vectors must be of same length.
'''

def component_wise_mean(vectors):
    # Ensure all vectors have the same length
    vector_length = len(vectors[0])
    assert all(len(vec) == vector_length for vec in vectors), "All vectors must have the same length"
    
    # Compute the component-wise mean
    mean_vector = [sum(component) / len(vectors) for component in zip(*vectors)]
    return mean_vector

# Example usage:
vectors = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mean = component_wise_mean(vectors)
print("Component-wise mean vector:", mean)

'''
Component-wise mean vector: [4.0, 5.0, 6.0]
'''