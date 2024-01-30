import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for letter in range(word_length):
    display.append("_")

print(logo)
print(f"{' '.join(display)}")


while "_" in display:
    guess = input("\nGuess a letter: ").lower()

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if (lives == 0):
            print(f'Pssst, the solution is {chosen_word}.')
            print('You Lose! 🏴‍☠️🏴‍☠️🏴‍☠️')
            break

    print(f"{' '.join(display)}")

if "_" not in display:
    print('You won! 🏆🏆🏆')
