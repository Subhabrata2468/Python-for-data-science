'''
what do you mean by delimited files? 
Create the tab delimited text file containing company name,
Number of students placed and the package of 5 software comapines 
and display them on the console using python program
'''

# Define the content for the tab-delimited file
data = """Company Name\tNumber of Students Placed\tPackage
Company A\t50\t12.5
Company B\t30\t10.0
Company C\t70\t15.0
Company D\t40\t11.0
Company E\t60\t14.0"""

# Write the content to a tab-delimited text file
with open('companies.txt', 'w') as file:
    file.write(data)

# Read and display the content from the tab-delimited text file
with open('companies.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())


'''
runfile('C:/Users/subha/.spyder-py3/temp.py', wdir='C:/Users/subha/.spyder-py3')
Company Name	Number of Students Placed	Package
Company A	t50	12.5
Company B	30	10.0
Company C	70	15.0
Company D	40	11.0
Company E	60	14.0
'''
