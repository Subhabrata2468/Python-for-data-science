'''An anonymous dataset containing each user’s salary (in dollars) and tenure as a data scientist (in years) is given.
salaries and tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5), (76000,
7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)]
Find out the average salary for each tenure and print a massage according to its value, i.e.,
” less than two”,” between two and five” and” more than five” 
tenure and group together the salaries corresponding to each bucket. Compute the average Salary for each group.'''
from collections import defaultdict

# Data: Salaries paired with respective tenures
salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5),
    (76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)
]

# Function to categorize tenure into buckets
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif 2 <= tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# Group salaries by tenure bucket
salary_by_tenure_bucket = defaultdict(list)  #empty list
#print(salary_by_tenure_bucket)

for salary, tenure in salaries_and_tenures:
    #print(tenure)
    bucket = tenure_bucket(tenure)
    #print(bucket)
    salary_by_tenure_bucket[bucket].append(salary)
#print(salary_by_tenure_bucket)

# Calculate average salary for each tenure bucket
average_salary_by_bucket = {}
for tenure_bucket, salaries in salary_by_tenure_bucket.items():
    #print(salaries)
    average_salary_by_bucket[tenure_bucket] = sum(salaries) / len(salaries)

# Print average salary for each tenure bucket
for bucket, average_salary in average_salary_by_bucket.items():
    print(f"Average Salary for {bucket} tenure: ${average_salary:.2f}")

''' OUTPUT
Average Salary for more than five tenure: $79166.67
Average Salary for less than two tenure: $48000.00
Average Salary for between two and five tenure: $61500.00
'''