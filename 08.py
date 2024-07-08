# 8)Write a Python program that imports a custom module you created with a function that returns 
# the factorial of a number.


from fact import fact

def main():
    n = int(input("Enter the number: "))
    result = fact(n)
    print("Factorial of your number is:", result)

if __name__ == "__main__":
    main()
