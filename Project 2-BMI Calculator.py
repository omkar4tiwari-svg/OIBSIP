# BMI Calculator

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

bmi = weight / (height ** 2)

print("\nYour BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")