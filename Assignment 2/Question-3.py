'''
Write two functions that extract the rows and columns of a matrix A.
'''


def extract_rows(matrix):
    return matrix

def extract_columns(matrix):
    num_columns = len(matrix[0])
    #print(num_columns)
    return [[row[i] for row in matrix] for i in range(num_columns)]

# Example usage:
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = extract_rows(matrix_A)
print("Rows of matrix A:", rows)

columns = extract_columns(matrix_A)
print("Columns of matrix A:", columns)

'''
Rows of matrix A: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Columns of matrix A: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
'''
