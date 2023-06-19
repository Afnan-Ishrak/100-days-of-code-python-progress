#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art
print(art.logo)
print("\nWelcome to the Number Guessing Game! \nI am thinking of a number between 1 to 100.\nGood luck guessing what the number is!")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

number = random.randint(1,100)

guess = ""
attempts = 0

if difficulty == "easy":
    attempts += 10
elif difficulty == "hard":
    attempts += 5

def check_number():
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")

game_not_end = True
while guess != number and game_not_end:
    print(f"You have {attempts} attempts remaining at guessing the number.")
    guess = int(input("Make a guess:"))
    check_number()
    if number != guess:
        attempts -= 1
    if attempts == 0:
        print("Sorry you have failed to guess the number. Better luck next time 😉")
        game_not_end = False
if guess == number:
    print(f"Congratulations! You have guessed the correct number: {number} !!!🥳")   
