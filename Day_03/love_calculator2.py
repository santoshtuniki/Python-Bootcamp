'''
To work out the love score between two people:

    Take both people's names and check for the number of times the letters in the word TRUE occurs.

    Then check for the number of times the letters in the word LOVE occurs.

    Then combine these numbers to make a 2 digit number.
'''

name1 = input('What is your name?\n')
name2 = input('What is their name?\n')

name = name1+name2
TRUE = 0
LOVE = 0

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

print("The Love Calculator is calculating your score...")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


