'''
write the python program to read from 'phone.txt' , a text file holding 
the mobiles numbers and print the valid mobile numbers based on the following
.the first digit should contain numbers between 6 to 9 
.The rest 9 digits can contain any number between 0 to 9
'''
import re

def is_valid_mobile_number(number):
    """
    Check if the mobile number is valid.
    The first digit should be between 6 to 9
    The rest 9 digits can be any number between 0 to 9.
    """
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, number) is not None

def read_and_validate_phone_numbers(file_path):
    valid_numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                number = line.strip()
                if is_valid_mobile_number(number):
                    valid_numbers.append(number)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    return valid_numbers

def main():
    file_path = 'phone.txt'
    valid_numbers = read_and_validate_phone_numbers(file_path)
    if valid_numbers:
        print("Valid mobile numbers:")
        for number in valid_numbers:
            print(number)
    else:
        print("No valid mobile numbers found.")

if __name__ == "__main__":
    main()
    

'''
input
'phone.txt'
9431566074
7992277943
5123648972
6259874315

output
Valid mobile numbers:
9431566074
7992277943
6259874315
'''
