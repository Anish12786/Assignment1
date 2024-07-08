# 10) Write a Python function that takes a list of numbers and returns the maximum value in the list.
 
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Check if the list is empty
if not numbers:
    max_value = None
else:
    max_value = max(numbers)

# Print the maximum value
print("The maximum value in the list is:", max_value)
