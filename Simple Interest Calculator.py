# Input principal amount, rate of interest, and time period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (as a percentage): "))
time = float(input("Enter the time period in years: "))

# Convert rate from percentage to decimal
rate = rate / 100

# Calculate simple interest
# Formula: simple interest = principal * rate * time
simple_interest = principal * rate * time

# Print the simple interest
print("The simple interest is:", simple_interest)
