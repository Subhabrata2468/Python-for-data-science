'''
Count frequencies of various alphabets (Convert upper case into lower case and input given by user), plot the results for this as a bar chart with x-axis being the letter and y-axis as the corresponding frequency.
'''
import matplotlib.pyplot as plt
from collections import defaultdict

# Step 1: Read input
input_string = input("Enter a string: ")

# Step 2: Convert to lowercase
input_string = input_string.lower()

# Step 3: Count frequencies
alphabet_freq = defaultdict(int)
for char in input_string:
    if char.isalpha():  # Check if the character is an alphabet
        alphabet_freq[char] += 1
        
sorted_dict = dict(sorted(alphabet_freq.items()))

# Step 4: Plot the results
letters = list(sorted_dict.keys())
frequencies = list(sorted_dict.values())

plt.bar(letters, frequencies)
plt.xlabel('Alphabet')
plt.ylabel('Frequency')
plt.title('Frequency of Alphabets')
plt.show()

'''
OUTPUT
Enter a string: ascxzcwewqfretyghtgfhbvmnmhgjkliukopuyvgutggdgwqaszcxxbdbmk
'''
