from art import logo
import random


def deal_card():
    '''Returns a random card from the deck'''
    # 11 is the Ace.
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card


def calculate_score(cards):
    '''Take a list of cards and return the score calculated from the cards'''
    # check for a blackjack (a hand with only 2 cards: ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has a BlackJack 😱"
    elif user_score == 0:
        return "Win with a BlackJack 😎"
    elif user_score > 21:
        return "You wnet over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return 'You win 😃'
    else:
        return 'You lose 😤'


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal the user and computer 2 cards each at the beginning
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # For the user to take cards
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "\nType 'y' to get another card, type 'n' to pass."
            )
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # To let computer continue to play
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}"
    )
    print(compare(user_score, computer_score))


while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
