# Rock, Paper, Scissors
# 1 Oct 2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Kayla Ward
# Import random
# Establish names for the random computere options
# Using the if function, assign values for each input
# Get a number from the user and determine who wins.

import random

def rps():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()

# Define function when computer chooses rock.
def computer_choice_rock():
    user_choice = input("1 for rock, 2 for paper, 3 for scissors: ")
    if user_choice == "1":
        print("You tie. You chose rock and the computer chose rock.")
        try_again()
    elif user_choice == "2":
        print("You win! The computer chose rock and you chose paper.")
        try_again()
    elif user_choice =="3":
        print("You lose. You chose scissors and the computer chose rock.")
        try_again()
    else:
        print("Try again.")
        computer_choice_rock()

# Define function when computer chooses paper.
def computer_choice_paper():
    user_choice = input("1 for rock, 2 for paper, 3 for scissors: ")
    if user_choice == "1":
        print("You lose. You chose rock and the computer chose paper.")
        try_again()
    elif user_choice == "2":
        print("You tie. You chose paper and the computer chose paper.")
        try_again()
    elif user_choice == "3":
        print("You win! The computer chose paper and you chose scissors.")
    else:
        try_again()
        computer_choice_paper()

# Define function when computer chooses scissors.
def computer_choice_scissors():
    user_choice = input("1 for rock, 2 for paper, 3 for scissors: ")
    if user_choice == "1":
        print("You win! The computer chose scissors and you chose rock.")
        try_again()
    elif user_choice == "2":
        print("You lose. You chose paper and the computer chose scissors.")
        try_again()
    elif user_choice == "3":
        print("You tie. The computer chose scissors and you chose scissors.")
        try_again()
    else:
        try_again()
        coputer_choice_scissors()

# Define try again function.
def try_again():
    choice = input("Would you like to play again? y/n ")
    if choice == "y":
        rps()
    elif choice == "n":
        print("Thanks for playing!")
        quit()
    else:
        print("Try again")
        try_again()

rps()
        
