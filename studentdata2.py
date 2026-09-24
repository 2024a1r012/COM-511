# 7.  Write a Python program to store multiple student records as a list of tuples. 
#     Each tuple should contain name, roll number, and marks.
#     Display students who scored above 75.
students = [
    ("Keshav", 101, 82),
    ("Chhavi", 102, 68),
    ("Bhumika", 103, 91),
    ("Roshni", 104, 74),
    ("Maniya", 105, 78)
]

print("All Student Records:")
print(students)

print("\nStudents scoring above 75:")
for student in students:
    name, roll_no, marks = student
    if marks > 75:
        print(f"Name: {name}, Roll No: {roll_no}, Marks: {marks}")
