# Input a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
# A year is a leap year if it is divisible by 4 but not by 100, except for years that are also divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # Print if the year is a leap year
    print(year, "is a leap year.")
else:
    # Print if the year is not a leap year
    print(year, "is not a leap year.")
