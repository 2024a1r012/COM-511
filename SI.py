#calculate simple interest and total amount using principal,rate,and time entered by user

p=int(input("Enter Principal:"))
r=int(input("Enter Rate:"))
t=int(input("Enter time:"))

SI=(p*r*t)/100
total=p+SI

print(f"Simple Interest:",SI)
print(f"Total Amount:",total)