# Input weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in feet: "))

# Convert height from feet to meters
# 1 foot = 0.3048 meters
height = height * 0.3048

# Calculate BMI
# BMI = weight / (height ** 2)
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))

# Determine BMI category
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
