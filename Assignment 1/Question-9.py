'''
Python Program to find all Numbers in a Range (given by user) which are 
Perfect Squares and Sum of all Digits in the Number is Less than 10.
'''
def is_perfect_square(num):
    return num ** 0.5 == int(num ** 0.5)

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def find_numbers_in_range(start, end):
    result = []
    for i in range(start, end + 1):
        if is_perfect_square(i) and sum_of_digits(i) < 10:
            result.append(i)
    return result

# Input range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Find and display numbers satisfying the conditions
result = find_numbers_in_range(start, end)
if result:
    print("Numbers in the range with sum of digits less than 10 and are perfect squares:")
    print(result)
else:
    print("No numbers found in the range with sum of digits less than 10 and are perfect squares.")


'''
OUTPUT
Enter the start of the range: 50
Enter the end of the range: 500
Numbers in the range with sum of digits less than 10 and are perfect squares:
[81, 100, 121, 144, 225, 324, 400, 441]
'''