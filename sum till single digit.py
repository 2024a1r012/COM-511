# 8.  Write a Python program to repeatedly calculate the sum of digits of a number 
#     until the result becomes a single digit.
#     Example: 9875→9+8+7+5=292+9=11→1+1=2

n=int(input("Enter your number:"))
while n>=10:
    sum=0
    while n>0:
        digit=n%10
        n=n//10
        sum=sum+digit
    n=sum
print("sum:",n)