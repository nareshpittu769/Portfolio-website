# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random

game_list = [rock,paper,scissor]

user_choise = int(input("Enter the number 0. Rock, 1. Paper, 2. Scissors : "))
if user_choise > 2 and user_choise < 0:
    print('Invalid number and You Loose..')
else:
    print('User Choose: ')
    print(game_list[user_choise])
    computer_choise = random.randint(0,2) 
    print(f"Computer chose: ")
    print(game_list[computer_choise])
    if user_choise == computer_choise:
        print(" It's a Draw")
    elif user_choise == 0 and computer_choise == 2:
        print('You Win..')
    elif user_choise == 2 and computer_choise == 0:
        print('You Loose..')
    elif user_choise > computer_choise:
        print('You Win..')
    elif user_choise < computer_choise:
        print('You Loose..')