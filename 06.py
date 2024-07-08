# 6)Write a Python program to check if a given number is prime or not.

num = int(input("Enter any number :"))

for i in range (2,num):
    if num % i == 0:
        print("Not prime")
        break

else:
    print("Prime")

