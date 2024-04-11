'''
Write a Python program to find the correlation of Math and Science marks.
'''

def mean(xs):
    return sum(xs) / len(xs)

def covariance(x, y):
    if len(x) != len(y):
        return "Length of datasets must be the same"
    x_mean=mean(x)
    y_mean=mean(y)
    covariance=sum((x[i]-x_mean)*(y[i]-y_mean) for i in range (len(x))) / (len(x)-1)
    return covariance

def correlation(x, y):
    if len(x) != len(y):
        return "Length of datasets must be the same"
    cov = covariance(x, y)
    dev_x = covariance(x, x) ** 0.5
    dev_y = covariance(y, y) ** 0.5
    correlation = cov / (dev_x * dev_y)
    return correlation


def main():
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
        {"student id": 20, "Math": 70, "Computer Science": 80, "Science": 75},
    ]

    math_marks = [student_data["Math"] for student_data in students]
    science_marks = [student_data["Science"] for student_data in students]

    covariance(math_marks, science_marks)
    print("correlation of Math and Science marks:",correlation(math_marks, science_marks))

if __name__ == "__main__":
    main()
'''
correlation of Math and Science marks: 0.6196285930399521
'''