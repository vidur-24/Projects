import random

user_wins = 0
comp_wins = 0
ties = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Rock/Paper/Scissors (or) enter q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)  # rock:0 paper:1 scissors:2
    computer_pick = options[random_number]

    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
    elif user_input == "paper " and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock" or user_input == "paper" and computer_pick == "paper" or user_input == "scissors" and computer_pick == "scissors":
        print("It's a tie!")
        ties += 1

    else:
        print("You Lost!")
        comp_wins += 1

print("Computer's score:", comp_wins)
print("Your score:", user_wins)
print("Tie's count:", ties)
print("Thank You for playing!")
