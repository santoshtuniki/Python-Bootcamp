import os
import random
from art import logo, vs
from game_data import data

game_over = False


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


indexA = randomIndex()

indexB = indexOfB(indexA)


