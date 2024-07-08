4) # 4.Write a Python program to swap the values of two variables without using a third variable. 

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print(f"Before swapping: first number = {a}, second number = {b}")

# Swapping using a temporary variable
temp = a
a = b
b = temp

print(f"After swapping: first number = {a}, second number = {b}")
