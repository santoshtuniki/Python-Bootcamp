from art import logo
import random

print(logo)


def deal_card():
    '''Returns a random card from the deck'''
    # 11 is the Ace.
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card


def calculate_score(cards):
    # check for a blackjack (a hand with only 2 cards: ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    return sum(cards)


user_cards = []
computer_cards = []

# Deal the user and computer 2 cards each at the beginning
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)

print(calculate_score(user_cards))
print(calculate_score(computer_cards))
