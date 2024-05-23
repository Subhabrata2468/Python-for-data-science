'''
Write a python program to split the data ’X’ into test and train dataset
and print them, use 70-30 split criteria.
'''
from sklearn.model_selection import train_test_split

# Step 1: Define or generate the dataset 'X'
# For demonstration, we'll use a list of numbers as the dataset.
X = list(range(1, 101))  # Dataset with 100 numbers

# Step 2: Split the dataset into training and testing sets
train, test = train_test_split(X, test_size=0.3, random_state=42)

# Step 3: Print the training and testing sets
print("Training set:", train)
print("Testing set:", test)

'''
output

Training set: [2, 95, 73, 85, 92, 51, 81, 6, 59, 33, 63, 34, 99, 54, 42, 48, 16, 72, 25, 20, 90, 98, 66, 49, 28, 23, 65, 60, 97, 15, 21, 84, 47, 87, 58, 83, 50, 76, 29, 13, 46, 69, 79, 78, 80, 74, 56, 14, 57, 27, 82, 37, 52, 77, 71, 88, 55, 67, 91, 86, 17, 4, 26, 24, 53, 45, 32, 18, 36, 19]
Testing set: [8, 93, 30, 22, 64, 3, 70, 40, 31, 11, 1, 12, 68, 10, 35, 94, 62, 96, 7, 9, 38, 100, 75, 41, 89, 43, 44, 61, 5, 39]


'''

'''
    Import the train_test_split function:
        from sklearn.model_selection import train_test_split: Imports the train_test_split function from sklearn.model_selection.

    Define the dataset X:
        X = list(range(1, 101)): Creates a list of numbers from 1 to 100.

    Split the dataset:
        train, test = train_test_split(X, test_size=0.3, random_state=42):
            X is the dataset to be split.
            test_size=0.3 specifies that 30% of the data should be in the test set.
            random_state=42 ensures reproducibility of the split.

    Print the training and testing sets:
        print("Training set:", train): Prints the training set.
        print("Testing set:", test): Prints the testing set.
'''