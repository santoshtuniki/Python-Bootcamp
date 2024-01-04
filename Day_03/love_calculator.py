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

for x in 'TRUE':
    for y in name:
        if y.lower() == x.lower():
            TRUE += 1

for x in 'LOVE':
    for y in name:
        if y.lower() == x.lower():
            LOVE += 1

score = str(TRUE)+str(LOVE)
score = int(score)

print("The Love Calculator is calculating your score...")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
