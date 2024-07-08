# 12) Write a Python program to count the number of vowels in a given string.



s = input("Please enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print(f"The number of vowels in the string is: {count}")
    