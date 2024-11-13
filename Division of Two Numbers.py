# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the second number is not zero to avoid division by zero error
if num2 != 0:
    # Calculate the result of division
    result = num1 / num2
    # Print the result
    print("The result of division is:", result)
else:
    # Print an error message if division by zero is attempted
    print("Error: Division by zero is not allowed.")
