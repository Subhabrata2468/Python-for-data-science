'''
Write a python program to create a Dataclass with following details 
(Roll No.,[Name,Branch,Year of Admission]).
'''
from dataclasses import dataclass

@dataclass
class Student:
    RollNo: int
    Name: str
    Branch: str
    YearOfAdmission: int

# Create instances of the Student dataclass
student1 = Student(RollNo=101, Name='Alice Smith', Branch='Computer Science', YearOfAdmission=2021)
student2 = Student(RollNo=102, Name='Bob Johnson', Branch='Mechanical Engineering', YearOfAdmission=2020)

# Print the details of the students
print(f'Student 1: Roll No. {student1.RollNo}, Name: {student1.Name}, Branch: {student1.Branch}, Year of Admission: {student1.YearOfAdmission}')
print(f'Student 2: Roll No. {student2.RollNo}, Name: {student2.Name}, Branch: {student2.Branch}, Year of Admission: {student2.YearOfAdmission}')


'''
output

Student 1: Roll No. 101, Name: Alice Smith, Branch: Computer Science, Year of Admission: 2021
Student 2: Roll No. 102, Name: Bob Johnson, Branch: Mechanical Engineering, Year of Admission: 2020

'''

'''
    Import the dataclass decorator:

    from dataclasses import dataclass: Imports the dataclass decorator from the dataclasses module.

    Define the Student dataclass:

    The @dataclass decorator is used to automatically generate special methods like __init__, __repr__, and __eq__ 
    for the class.
    The Student class has four attributes: RollNo (int), Name (str), Branch (str), and YearOfAdmission (int).

    Create instances of the Student dataclass:

    student1 and student2 are instances of the Student class, with values assigned to their attributes.

    Print the details of the students:

    The attributes of each Student instance are accessed and printed.
'''