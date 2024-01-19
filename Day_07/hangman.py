import random
from execution import stages

word_list = ["aardvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for letter in range(word_length):
    display.append("_")

print(display)

while "_" in display:
    guess = input("\nGuess a letter: ").lower()

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        if (lives == 0):
            print(stages[lives])
            print('You Lose!')
            break
        else:
            print(stages[lives+1])

    print(display)

if "_" not in display:
    print('You won!')
