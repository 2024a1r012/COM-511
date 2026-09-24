# 1.  Write a Python program to store all month names in a tuple.
#     Input a month number and display the corresponding month name.

months=("January","February","March","April","May","June","July","August",
        "September","october","November","December")

month_no=int(input("enter month Number:"))

if month_no>=1 and month_no<=12:
    print("Month:",months[month_no-1])