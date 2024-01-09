target = int(input("Enter a number between 0 and 1000:\n"))

if target <= 0 or target >= 1000:
    print("Sorry!...Only numbers between 0 to 1000 are allowed.")
else:
    even_sum = 0
    for number in range(2, target + 1, 2):
        even_sum += number
    print(even_sum)
