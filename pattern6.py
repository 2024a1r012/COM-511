# 14. write a python program to print a centered pyramid using stars
#           *
#         * * *
#       * * * * * 
#     * * * * * * * 
    
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)