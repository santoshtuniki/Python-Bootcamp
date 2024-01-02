height = input("Enter your height in meters: \n")
weight = input("Enter your weight in kilograms: \n")

height = float(height)
weight = float(weight)

bmi = int(weight / height ** 2)
print(f"Your BMI: \n{bmi}")
