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

import random

random_integer = random.randint(0,2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

#display player choice
if player_choice == 0:
    print(rock)

if player_choice == 1:
    print(paper)

if player_choice == 2:
    print(scissors)

print("Computer choose:")
#display computer choice
if random_integer == 0:
    print(rock)

if random_integer == 1:
    print(paper)

if random_integer == 2:
    print(scissors)

#Check who wins
if player_choice == random_integer:
    print("draw")
elif player_choice == 0:
    if random_integer == 1:
        print("You lose")
    else:
        print("You win")
elif player_choice == 1:
    if random_integer == 2:
        print("You lose")
    else:
        print("You win")
elif player_choice == 2:
    if random_integer == 0:
        print("You lose")
    else:
        print("You win")
