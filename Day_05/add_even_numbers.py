target = int(input("Enter a number between 0 and 1000:\n"))

if target <= 0 or target >= 1000:
    print("Sorry!...Only numbers between 0 to 1000 are allowed.")
else:
    sum = 0
    for x in range(1, target+1):
        if x % 2 == 0:
            sum += x
    else:
        print(sum)
