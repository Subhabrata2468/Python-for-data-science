'''

Write a Python program to group the student ids corresponding to the following Science mark.
• less or equal to 30.
• between 30 and 70.
• more than 70.

'''

from collections import defaultdict

students = [
    {"student id": 1, "Math": 50, "Computer Science": 60, "Science": 73},
    {"student id": 2, "Math": 40, "Computer Science": 50, "Science": 55},
    {"student id": 3, "Math": 90, "Computer Science": 70, "Science": 95},
    {"student id": 4, "Math": 80, "Computer Science": 62, "Science": 72},
    {"student id": 5, "Math": 80, "Computer Science": 90, "Science": 45},
    {"student id": 6, "Math": 84, "Computer Science": 90, "Science": 50},
    {"student id": 7, "Math": 90, "Computer Science": 95, "Science": 55},
    {"student id": 8, "Math": 89, "Computer Science": 93, "Science": 53},
    {"student id": 9, "Math": 88, "Computer Science": 92, "Science": 58},
    {"student id": 10, "Math": 90, "Computer Science": 95, "Science": 55},
    {"student id": 11, "Math": 70, "Computer Science": 65, "Science": 39},
    {"student id": 12, "Math": 65, "Computer Science": 60, "Science": 35},
    {"student id": 13, "Math": 60, "Computer Science": 55, "Science": 30},
    {"student id": 14, "Math": 55, "Computer Science": 57, "Science": 25},
    {"student id": 15, "Math": 49, "Computer Science": 54, "Science": 22},
    {"student id": 16, "Math": 10, "Computer Science": 30, "Science": 11},
    {"student id": 17, "Math": 50, "Computer Science": 40, "Science": 16},
    {"student id": 18, "Math": 90, "Computer Science": 45, "Science": 80},
    {"student id": 19, "Math": 70, "Computer Science": 50, "Science": 39},
    {"student id": 20, "Math": 70, "Computer Science": 80, "Science": 75}
]

def marks(integer):
    if integer <30:
        return "less or equal to 30"
    elif integer >=30 and integer <=70:
        return "between 30 and 70"
    elif integer >70:
        return "more_than_70"
    
newdict=defaultdict(list)
for std in students:
    science_marks=std["Science"]
    newdict[marks(science_marks)].append(std["student id"])

#print(newdict)

for comment,ids in newdict.items():
    print(f"Those students who score {comment} are{ids}")

'''
Those students who score more_than_70 are[1, 3, 4, 18, 20]
Those students who score between 30 and 70 are[2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 19]
Those students who score less or equal to 30 are[14, 15, 16, 17]
'''