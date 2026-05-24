import random

items = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0

print("=== Rock Paper Scissor Game ===")

for i in range(5):

    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissor")

    user = int(input("Enter your choice: "))

    if user == 1:
        user_choice = "rock"

    elif user == 2:
        user_choice = "paper"

    elif user == 3:
        user_choice = "scissor"

    else:
        print("Invalid Input")
        continue

    computer_choice = random.choice(items)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("Match Draw")
        user_score += 1
        computer_score += 1

    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        print("You Win")
        user_score += 2

    else:
        print("Computer Wins")
        computer_score += 2

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

print("\n=== Final Result ===")

if user_score > computer_score:
    print("You won the game")

elif computer_score > user_score:
    print("Computer won the game")

else:
    print("Game Draw")