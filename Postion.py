#5. Write a python program to check whether a given value is present in a tuple. If present display its position
my_tuple = (10, 25, 30, 45, 50, 65)
target = int(input("Enter the value to search: "))
found = False
for i in range(len(my_tuple)):
    if my_tuple[i] == target:
        print(f"Value {target} is present at index/position {i}.")
        found = True
        break
if not found:
    print(f"Value {target} is not present in the tuple.")