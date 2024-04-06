'''
For the above data there seems to be a correspondence between years of experience and
paid accounts users with very few and very many years of experience tend to pay; users with
average amounts of experience don’t. Find out the condition for this correspondence and print
it.
'''
# Data: Salaries paired with respective tenures
salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5),
    (76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)
]

# Function to determine if the user tends to pay based on tenure
def tends_to_pay(tenure):
    if tenure < 2 or tenure > 5:
        return True
    else:
        return False


# Test the condition for each tenure in the dataset
for salary, tenure in salaries_and_tenures:
    if tends_to_pay(tenure):
        print(f"For a tenure of {tenure} years, the user tends to pay.")
    else:
        print(f"For a tenure of {tenure} years, the user does not tend to pay.")
        
'''
For a tenure of 8.7 years, the user tends to pay.
For a tenure of 8.1 years, the user tends to pay.
For a tenure of 0.7 years, the user tends to pay.
For a tenure of 6 years, the user tends to pay.
For a tenure of 6.5 years, the user tends to pay.
For a tenure of 7.5 years, the user tends to pay.
For a tenure of 2.5 years, the user does not tend to pay.
For a tenure of 10 years, the user tends to pay.
For a tenure of 1.9 years, the user tends to pay.
For a tenure of 4.2 years, the user does not tend to pay.
'''
