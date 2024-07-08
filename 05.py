# 5) Write a Python program to print the first 10 numbers of the Fibonacci series. 

a = 1
b = 1
c = a + b
print("The numbers of the series are:")

for i in range(0, 10):
    print(a)
    a = b
    b = c
    c = a + b 
