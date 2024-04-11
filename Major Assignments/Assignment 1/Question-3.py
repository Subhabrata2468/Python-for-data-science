
'''
Write a Python program to create a list of 20 vectors by taking student’s Math, Computer Science
and Science marks. Find the sum of all these 20 vectors. After that, find the average marks for M ath,
Computer Science and Science.
Hint: [50,60,73] will be one vector.
'''

vectors = [
    [50, 60, 73], [40, 50, 55], [90, 70, 95], [80, 62, 72], [80, 90, 45],
    [84, 90, 50], [90, 95, 55], [89, 93, 53], [88, 92, 58], [90, 95, 55],
    [70, 65, 39], [65, 60, 35], [60, 55, 30], [55, 57, 25], [49, 54, 22],
    [10, 30, 11], [50, 40, 16], [90, 45, 80], [70, 50, 39], [70, 80, 75]
]

sum_vector = [0, 0, 0]
num_students = len(vectors)

for vector in vectors:
    sum_vector[0] += vector[0]  
    sum_vector[1] += vector[1]  
    sum_vector[2] += vector[2]  

avg_math = sum_vector[0] / num_students
avg_cs = sum_vector[1] / num_students
avg_science = sum_vector[2] / num_students

print("Sum of all 20 vectors:", sum_vector)
print("Average marks - Math:", avg_math)
print("Average marks - Computer Science:", avg_cs)
print("Average marks - Science:", avg_science)
