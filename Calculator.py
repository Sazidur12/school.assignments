# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Select operator
print("Select operator: +, -, *, /, %")
operator = input()

# Perform calculation based on the operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero!")
        result = None
elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"The remainder is: {result}")
    else:
        print("Error: Division by zero!")
        result = None
else:
    print("Invalid operator selected!")
    result = None

# Print the result if it's not None and the operator is not "%"
if result is not None and operator != "%":
    print(f"The result of the operation is: {result}")
