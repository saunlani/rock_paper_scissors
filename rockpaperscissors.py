import random
import sys

while True:
    print("Welcome to Rock, Paper Scissors!")

    user_options = ["rock", "paper", "scissors"]
    cpu_options = ["Rock", "Paper", "Scissors"]
    leave_game = ["No", "n", "no"]
    stay_game = ["Yes", "y", "yes"]
    print("Rock, Paper or Scissors?")
    user_choice = input().lower()

    if user_choice not in user_options:
        print(" ")
        print("You didn't make a valid selection, ya Bobo.")
        print("Try again.")
        continue

    cpu_choice = random.choice(cpu_options)
    print(cpu_choice)

    if user_choice == cpu_choice.lower():
        print(" ")
        print("Draw!")
        continue

    if user_choice == 'scissors' and cpu_choice == 'Paper':
        print(" ")
        print("You win!")
        print('Type exit to exit, type anything else to play again.')
        response = input()
        if response == 'exit':
            sys.exit()
        else:
            continue

    if user_choice == 'rock' and cpu_choice == 'Scissors':
        print(" ")
        print("You win!")
        print('Type exit to exit, type anything else to play again.')
        response = input()
        if response == 'exit':
            sys.exit()
        else:
            continue

    if user_choice == 'paper' and cpu_choice == 'Rock':
        print(" ")
        print("You win!")
        print('Type exit to exit, type anything else to play again.')
        response = input()
        if response == 'exit':
            sys.exit()
        else:
            continue

    else:
        print(" ")
        print("You lose!")
        print('Type exit to exit, type anything else to play again.')
        response = input()
        if response == 'exit':
            sys.exit()
        else:
            continue
