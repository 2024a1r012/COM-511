# 6.  Write a Python program to store one student data as a tuple: 
#     name, roll number, and marks. Display grade based on marks.

name = input("Enter name: ")
roll = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))

student = (name, roll, marks)

if student[2] >= 90:
    grade = "A"
elif student[2] >= 75:
    grade = "B"
elif student[2] >= 50:
    grade = "C"
else:
    grade = "F"

print("Student Data:", student)
print("Grade:", grade)