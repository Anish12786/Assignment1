# 13) 13) Write a Python program that prints a multiplication table up to (numberx10).

num = int(input("Enter the number for which you want the multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
