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

player_choice = input("What do you pick? Rock, Paper or Scissors?").lower()
options = ["rock", "paper", "scissors"]
ascii_options = [rock, paper, scissors]
computer_choice = random.choice(options)
print("\nYou CHOSE:\n"+player_choice.upper())


if player_choice == computer_choice:
    print("\nComputer chose:\n"+computer_choice.upper())
    print("It is a TIE!!!")
elif player_choice=="rock": 
  print(rock)
  if computer_choice=="scissors":
    print("Computer chose:\n"+scissors)
    print("You win. Rock breaks scissors.")
  else:
    print("Computer chose:\n"+paper)
    print("You lose. Paper engulfs scissors.")
elif player_choice=="paper":
  print(paper)
  if computer_choice=="rock":
    print("Computer chose:\n"+rock)
    print("You win. Paper engulfs scissors.")
  else:
    print("Computer chose:\n"+scissors)
    print("You lose. Scissors cut paper.")
elif player_choice=="scissors": 
  print(scissors)
  if computer_choice=="paper":
    print("Computer chose:\n"+paper)
    print("You win. Scissors cut paper.")
  else:
    print("Computer chose:\n"+rock)
    print("You lose. Rock breaks scissors.")