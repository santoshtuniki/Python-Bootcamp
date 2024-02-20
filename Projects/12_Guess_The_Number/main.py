import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'hard':
        return HARD_LEVEL_TURNS
    elif level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        print('Choose between easy & hard only.\n')
        set_difficulty()


def check_answer(guess, answer, turns):
    '''Checks answer against guess. Retuns the number of turns remaining.'''
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, You lose!")
            return

game()