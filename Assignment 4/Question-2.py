'''
Write a python program to create a NamedTuple with following details 
(Roll No.,[Name,Branch,Year of Admission]).
'''
from collections import namedtuple

# Step 1: Define the NamedTuple
Student = namedtuple('Student', ['RollNo', 'Name', 'Branch', 'YearOfAdmission'])

# Step 2: Create instances of the NamedTuple
student1 = Student(RollNo=101, Name='Alice Smith', Branch='Computer Science', YearOfAdmission=2021)
student2 = Student(RollNo=102, Name='Bob Johnson', Branch='Mechanical Engineering', YearOfAdmission=2020)

# Step 3: Access the fields
print(f'Student 1: Roll No. {student1.RollNo}, Name: {student1.Name}, Branch: {student1.Branch}, Year of Admission: {student1.YearOfAdmission}')
print(f'Student 2: Roll No. {student2.RollNo}, Name: {student2.Name}, Branch: {student2.Branch}, Year of Admission: {student2.YearOfAdmission}')


'''
output

Student 1: Roll No. 101, Name: Alice Smith, Branch: Computer Science, Year of Admission: 2021
Student 2: Roll No. 102, Name: Bob Johnson, Branch: Mechanical Engineering, Year of Admission: 2020

'''

'''
    Define the NamedTuple:

    Student = namedtuple('Student', ['RollNo', 'Name', 'Branch', 'YearOfAdmission']) creates a NamedTuple called Student with fields RollNo, Name, Branch, and YearOfAdmission.

    Create instances:

    student1 = Student(RollNo=101, Name='Alice Smith', Branch='Computer Science', YearOfAdmission=2021) creates an instance of Student with specified values.
    Similarly, student2 is another instance.

    Access fields:

    student1.RollNo, student1.Name, student1.Branch, student1.YearOfAdmission are used to access the values of each field for student1.
    Print statements are used to display the information
'''