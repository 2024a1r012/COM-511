# 4.  Write a Python program to store repeated values in a tuple and count how many times a given value appears.

numbers = (10, 20, 30, 20, 40, 20, 50, 10, 20)
print("Tuple elements:", numbers)
target = int(input("Enter the value to count: "))
count = numbers.count(target)
print(f"The value {target} appears {count} times in the tuple.")