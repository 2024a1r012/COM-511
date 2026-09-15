# 5.  write a python program to input a number and rverse it using arithemetic operation only  

n=int(input("Enter your number"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10

print("Reversed number:",rev)