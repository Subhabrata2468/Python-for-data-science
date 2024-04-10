'''
Write a program that takes the order of the matrix and 
creates a matrix in the following manner: The (ij)th entry of the matrix 
should be the sum of i and j. Eg: The 0th row and 0 th column should have the value (0+0) 
i.e. 0 and the 0 th row and
first column should have value (0+1) i.e. 1 and so on
'''
def create_matrix(order):
    matrix = []
    for i in range(order):
        row = []
        for j in range(order):
            row.append(i + j)
        matrix.append(row)
        
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    order = int(input("Enter the order of the matrix: "))
    if order <= 0:
        print("Invalid input. Order should be a positive integer.")
        return
    
    result_matrix = create_matrix(order)
    print("Matrix:")
    print_matrix(result_matrix)

if __name__ == "__main__":
    main()

'''
Enter the order of the matrix: 5
Matrix:
[0, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
[2, 3, 4, 5, 6]
[3, 4, 5, 6, 7]
[4, 5, 6, 7, 8]
'''