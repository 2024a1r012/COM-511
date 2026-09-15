# 3.  write a python program to check whether a number is a perfect number.
#     A number is perfect if the sum of its proper divisors is equal to the number itself

num=int(input("Enter your number:"))
sum_divisor=0
for i in range(1,num):
    if num%i==0:
        sum_divisor+=i

if sum_divisor==num:
    print("The number is a perfect number")
else:
    print("the number is not a perfect number")

