# 5.  Write a Python program to input a decimal number
#     and convert it into binary without using the built-in bin() function.

num=int(input("Enter number:"))
b=""
while num>0:
    r=num%2
    b=str(r)+b
    num=num//2
print("Binary number:",b)
