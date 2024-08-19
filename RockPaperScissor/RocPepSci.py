import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = None


while player not in choices:
    player = input("Rock, Paper, or Scissors?: ").lower()


print("Player plays: ", player)
print("Computer plays: ", computer)


if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins! You lose!")
