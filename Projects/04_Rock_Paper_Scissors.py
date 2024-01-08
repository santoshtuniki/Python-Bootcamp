import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(
    input("What do you choose?:\n0: Rock\n1: Paper\n2: Scissors\n\n")
)
computer_choice = random.randint(0, 2)

if user_choice not in [1, 2, 3]:
    print('You typed an invalid number!')
    print('You lose! 😭😭😭')
else:
    game_options = [rock, paper, scissors]
    print('You chose: \n', game_options[user_choice])
    print('Computer chose: \n', game_options[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print('You win! 🏆🏆🏆')
    elif user_choice == 1 and computer_choice == 0:
        print('You win! 🏆🏆🏆')
    elif user_choice == 2 and computer_choice == 1:
        print('You win! 🏆🏆🏆')
    elif user_choice == computer_choice:
        print('Tie Game!')
    else:
        print('Computer wins! 🖥️🖥️🖥️')
