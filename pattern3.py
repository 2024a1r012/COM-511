# 11. write a python programm to print a right angled triangeled using stars.
    # * 
    # * * 
    # * * * 
    # * * * *

n = int(input("Enter the value of n:"))
for i in range(1,n+1):
     for j in range(i): 
        print("*", end=" ") 
     print()
