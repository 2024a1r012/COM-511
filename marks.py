sub1=int(input("Enter 1st subject marks="))
sub2=int(input("Enter 2nd subject marks="))
sub3=int(input("Enter 3rd subject marks="))

avg=(sub1+sub2+sub3)/3

if(sub1>40 and sub2>40 and sub3>40 and avg>50):
    print(True)
else:
    print(False)