#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random as r

EASY = 10
HARD = 5
MIN_NUM = 1
MAX_NUM = 100
GAME_FLAG = False
SHOW_ANS = True


def boot_up():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  number = r.randint(MIN_NUM,MAX_NUM)
  if SHOW_ANS == True:
    print(f"Pssst, the correct answer is {number}")
  attempts = difficulty()
  return number, attempts


def difficulty():
  select = ''
  while select != 'easy' or select != 'hard':
    select = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if select == 'easy':
      return EASY
    elif select == 'hard':
      return HARD
    else:
      print("Invalid input.\n")

def make_guess(number,attempts,guess):
  if guess < number:
    print("Too Low.")
    attempts -= 1
    return attempts, False
  elif guess > number:
    print("Too High.")
    attempts -= 1
    return attempts, False
  elif guess == number:
    return attempts, True


number,attempts = boot_up()
while GAME_FLAG == False and attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  attempts,GAME_FLAG = make_guess(number,attempts,int(input("Make a guess: ")))
  print("Guess again.")

if attempts < 1:
  print("You've run out of guesses, you lose.")
else:
  print(f"You got it! The answer was {number}\n")


