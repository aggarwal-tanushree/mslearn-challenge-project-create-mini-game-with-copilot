# create a multi-player python game for 'rock, paper, scissors'. 'rock' beats 'scissors'. 'scissors' beats 'paper'. 'paper' beats 'rock' User should enter input in lowercases only for the input list [rock, paper, scissors]. If user enters an invalid input, he should be prompted and asked to reinput. Dsplay the winner at the end of the round.
# The game should be played in a loop until the user decides to quit. At the end of each round, the user should be prompted to play again. If the user decides to quit, display the number of wins and losses for the user.
# If the user enters 'quit' as the input, display the number of wins and losses for the user and quit the game.
# Sample Output:
# Enter your choice: rock
# Computer's choice: paper
# You lose!
# Do you want to play again? yes
# Enter your choice: paper
# Computer's choice: paper
# It's a tie!
# Do you want to play again? yes
# Enter your choice: scissors
# Computer's choice: rock
# You lose!
# Do you want to play again? no
# You won 0 times and lost 2 times.
# Goodbye!

import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input, try again.")
        continue

    random_number = random.randint(0, 2)
    # 0 is rock, 1 is paper, 2 is scissors
    if random_number == 0:
        computer = 'rock'
    elif random_number == 1:
        computer = 'paper'
    else:
        computer = 'scissors'

    print("Computer picked", computer + ".")

    if user_input == computer:
        print("It's a tie!")
    elif user_input == 'rock' and computer == 'scissors':
        print("You won!")
        user_wins += 1
    elif user_input == 'paper' and computer == 'rock':
        print("You won!")
        user_wins += 1
    elif user_input == 'scissors' and computer == 'paper':
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
import random
import sys

user_wins = 0
user_loss = 0