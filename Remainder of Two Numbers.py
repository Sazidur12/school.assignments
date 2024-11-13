# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if the second number is not zero to avoid division by zero error
if num2 != 0:
    # Calculate the remainder
    remainder = num1 % num2
    # Print the remainder
    print("The remainder when", num1, "is divided by", num2, "is:", remainder)
else:
    # Print an error message if division by zero is attempted
    print("Error: Division by zero is not allowed.")
