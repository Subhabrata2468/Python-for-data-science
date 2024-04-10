'''
Write a menu-driven program to perform 
Addition, Subtraction, 
Scalar Multiplication, Dot Product and Length of vectors.
'''

import math

def vector_addition(vector1, vector2):
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

def vector_subtraction(vector1, vector2):
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

def scalar_multiplication(scalar, vector):
    return [scalar * v for v in vector]

def dot_product(vector1, vector2):
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

def vector_length(vector):
    return math.sqrt(sum(v ** 2 for v in vector))

def main():
    print("Vector Operations Program")
    print("========================")
    
    while True:
        print("\nMenu:")
        print("1. Vector Addition")
        print("2. Vector Subtraction")
        print("3. Scalar Multiplication")
        print("4. Dot Product")
        print("5. Vector Length")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            vector1 = [float(x) for x in input("Enter vector 1 (comma separated): ").split(',')]
            vector2 = [float(x) for x in input("Enter vector 2 (comma separated): ").split(',')]
            result = vector_addition(vector1, vector2)
            print("Result of Vector Addition:", result)
        elif choice == '2':
            vector1 = [float(x) for x in input("Enter vector 1 (comma separated): ").split(',')]
            vector2 = [float(x) for x in input("Enter vector 2 (comma separated): ").split(',')]
            result = vector_subtraction(vector1, vector2)
            print("Result of Vector Subtraction:", result)
        elif choice == '3':
            scalar = float(input("Enter scalar: "))
            vector = [float(x) for x in input("Enter vector (comma separated): ").split(',')]
            result = scalar_multiplication(scalar, vector)
            print("Result of Scalar Multiplication:", result)
        elif choice == '4':
            vector1 = [float(x) for x in input("Enter vector 1 (comma separated): ").split(',')]
            vector2 = [float(x) for x in input("Enter vector 2 (comma separated): ").split(',')]
            result = dot_product(vector1, vector2)
            print("Result of Dot Product:", result)
        elif choice == '5':
            vector = [float(x) for x in input("Enter vector (comma separated): ").split(',')]
            result = vector_length(vector)
            print("Length of the Vector:", result)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()

'''
Vector Operations Program
========================

Menu:
1. Vector Addition
2. Vector Subtraction
3. Scalar Multiplication
4. Dot Product
5. Vector Length
6. Exit

Enter your choice (1-6): 1
Enter vector 1 (comma separated): 5,5,2
Enter vector 2 (comma separated): 5,3,6
Result of Vector Addition: [10.0, 8.0, 8.0]

Menu:
1. Vector Addition
2. Vector Subtraction
3. Scalar Multiplication
4. Dot Product
5. Vector Length
6. Exit

Enter your choice (1-6): 6
Exiting program...
'''
