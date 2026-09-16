# 10. write a python programm to print a square pattern of stars forn rows and n columns.
    # * * * *
    # * * * *
    # * * * *
    # * * * *

n=int(input("Enter Number of rows:"))
m=int(input("Enter Number of columns:"))

for i in range(n):
    for j in range(m):
        print("*",end=" ")
    print()
