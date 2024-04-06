'''
Write a Python Script to generate random passwords (alphanumeric). Ask users to enter the length of
password and number of passwords they want to generate and then print all the generated passwords.
'''
import random
import string

def generate_random_password(length):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits
    
    # Generate a random password of the specified length
    #The underscore _ is often used as a placeholder for 
    #loop variables when their values are not needed.
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Ask the user for the length of the password
    length = int(input("Enter the length of the password: "))
    
    # Ask the user for the number of passwords to generate
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate and print the specified number of passwords
    for i in range(num_passwords):
        password = generate_random_password(length)
        print(f"Password {i+1}: {password}")

if __name__ == "__main__":
    main()
    
    
'''
OUTPUT
Enter the length of the password: 7
Enter the number of passwords to generate: 5
Password 1: 9NFTcEh
Password 2: 4Q5tvyJ
Password 3: ijdTxPP
Password 4: QBE85MB
Password 5: x3HHagd
'''
