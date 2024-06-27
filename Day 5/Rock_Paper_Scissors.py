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
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game = ["rock", "paper", "scissors"]
length_game = len(game)
random_value = random.randint(0, length_game - 1)
computer_choose = game[random_value]
if user_input == 0:
    print(rock)
    print("Computer choose:")
    if computer_choose == "rock":
        print(rock)
        print("Match Draw")
    elif computer_choose == "paper":
        print(paper)
        print("You Lose, Paper Win")
    elif computer_choose == "scissors":
        print(scissors)
        print("You Win, Scissors Lose")
elif user_input == 1:
    print(paper)
    print("Computer choose:")
    if computer_choose == "rock":
        print(rock)
        print("You Win, Rock Lose")
    elif computer_choose == "paper":
        print(paper)
        print("Match Draw")
    elif computer_choose == "scissors":
        print(scissors)
        print("You Lose, Scissors Win")
elif user_input == 2:
    print(scissors)
    print("Computer choose:")
    if computer_choose == "rock":
        print(rock)
        print("you lose,Rock Win")
    elif computer_choose == "paper":
        print(paper)
        print("you Win,Paper lose")
    elif computer_choose == "scissors":
        print(scissors)
        print("Match Draw")
else:
    print("You Typed Invalid Number")
