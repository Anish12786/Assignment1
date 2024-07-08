# 2) Write a Python program that converts a given decimal number to its binary equivalent.

dec = int(input("Enter the decimal number: "))
binary = bin(dec)[2:]
print("Binary equivalent of your number is:", binary)
