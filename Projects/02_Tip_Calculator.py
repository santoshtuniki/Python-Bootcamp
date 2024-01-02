print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

people = input("How many people to split the bill? ")

bill_float = float(bill)

percentage_float = float(percentage)

people_float = float(people)

tip = bill_float * percentage_float / 100

total = bill_float + tip

# bill_per_person = round(total / people_float, 2)

# print(f"Each person should pay: ${bill_per_person}")

bill_per_person = total / people_float

print(f"Each person should pay: ${bill_per_person:.2f}")
