def prime_checker(number):
    for num in range(2, number):
        if (number % num == 0):
            print("It's not a prime number.")
            return
    print("It's a prime number.")


n = int(input("Enter a number:\n"))
prime_checker(number=n)
