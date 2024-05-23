'''
Given below is a confusion matrix, compute Precision, Recall, Accuracy and f1 score.

Confusion Matrix   Fit Unfit
Predict ’Fit’      250 750
Predict ’Unfit’    500 250
Write a python program using a generic function to compute above given parameters by taking values
of TP, FP, TN, FN as user input.
'''
def compute_metrics(TP, FP, TN, FN):
    # Compute Precision
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    # Compute Recall
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    # Compute Accuracy
    accuracy = (TP + TN) / (TP + FP + TN + FN) if (TP + FP + TN + FN) != 0 else 0
    # Compute F1 Score
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    
    return precision, recall, accuracy, f1_score

# Get user inputs
TP = int(input("Enter the number of True Positives (TP): "))
FP = int(input("Enter the number of False Positives (FP): "))
TN = int(input("Enter the number of True Negatives (TN): "))
FN = int(input("Enter the number of False Negatives (FN): "))

# Compute metrics
precision, recall, accuracy, f1_score = compute_metrics(TP, FP, TN, FN)

# Print the results
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"Accuracy: {accuracy:.2f}")
print(f"F1 Score: {f1_score:.2f}")

# For the given confusion matrix:
# Fit Unfit
# Predict 'Fit'      250 750
# Predict 'Unfit'    500 250
# The values are:
TP = 250
FP = 750
TN = 250
FN = 500

# Compute metrics for the given confusion matrix
precision, recall, accuracy, f1_score = compute_metrics(TP, FP, TN, FN)

# Print the results for the given confusion matrix
print("\nFor the given confusion matrix:")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"Accuracy: {accuracy:.2f}")
print(f"F1 Score: {f1_score:.2f}")

'''
output

Enter the number of True Positives (TP): 250
Enter the number of False Positives (FP): 750
Enter the number of True Negatives (TN): 250
Enter the number of False Negatives (FN): 500
Precision: 0.25
Recall: 0.33
Accuracy: 0.33
F1 Score: 0.29

For the given confusion matrix:
Precision: 0.25
Recall: 0.33
Accuracy: 0.33
F1 Score: 0.29

'''

'''
       Function compute_metrics:
        Computes Precision as Precision=   TP/(TP+FP)
        Computes Recall as Recall=         TP/(TP+FN)
        Computes Accuracy as Accuracy=    (TP+TN)/(TP+FP+TN+FN)
        Computes F1 Score as F1 Score=    (2×Precision×Recall) / (Precision+Recall)​
        Each metric includes a check to avoid division by zero.

    User inputs:
        The user is prompted to enter the values for TP, FP, TN, and FN.

    Printing the results:
        The program computes and prints Precision, Recall, Accuracy, and F1 Score with two decimal places.

    Predefined values for the given confusion matrix:
        The confusion matrix values are used to compute and print the metrics specifically for the provided confusion matrix.
'''