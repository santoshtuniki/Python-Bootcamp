import os
import random
from art import logo, vs
from game_data import data

game_over = False
score = 0


def clear():
    '''Clears the terminal'''
    os.system('cls||clear')


def randomIndex():
    '''Returns a random index value in the range of game data'''
    return random.randint(0, len(data)-1)


def indexOfB(indexA):
    '''Returns a index value of B which is not the index of A'''
    index = randomIndex()
    while index != indexA:
        return index


def description(index):
    '''Returns the string describing the comparison'''
    data_selected = data[index]
    return (f"{data_selected['name']}, a {data_selected['description']}, from {data_selected['country']}")


def compare(indexA, indexB):
    '''Returns the one with the highest follower count'''
    dataA = data[indexA]
    dataB = data[indexB]

    if dataA["follower_count"] > dataB["follower_count"]:
        return 'a'
    else:
        return 'b'


indexA = randomIndex()


while not game_over:
    clear()
    print(logo)

    print(f"Compare A: {description(indexA)}")
    print(vs)

    indexB = indexOfB(indexA)
    print(f"Compare B: {description(indexB)}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    result = compare(indexA, indexB)
    
    if user_choice == result:
        score += 1
        indexA = indexB
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
