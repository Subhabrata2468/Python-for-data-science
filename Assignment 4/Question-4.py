'''
Write, execute and visualise the progress of a python code using 
tqdm module with setting proper description.
'''
import time
from tqdm import tqdm

# Example task: Simulate processing a list of numbers
numbers = list(range(1, 101))  # A list of 100 numbers

# Use tqdm to visualize progress
for number in tqdm(numbers, desc="Processing numbers", unit="number"):
    # Simulate some processing task
    time.sleep(0.05)  # Sleep for 50 milliseconds

print("Processing complete!")


'''
output

Processing complete!

'''

'''
    Import necessary modules:
        time: Used to simulate a delay in processing.
        tqdm: Used to display the progress bar.

    Generate a list of numbers:
        numbers = list(range(1, 101)) creates a list of numbers from 1 to 100.

    Use tqdm to visualize progress:
        tqdm(numbers, desc="Processing numbers", unit="number") wraps the numbers list with a progress bar.
        desc="Processing numbers" sets a description for the progress bar.
        unit="number" specifies the unit for each iteration.

    Simulate a processing task:
        time.sleep(0.05) simulates a processing delay of 50 milliseconds per number.

    Print a completion message:
        After the loop finishes, a completion message is printed.
'''