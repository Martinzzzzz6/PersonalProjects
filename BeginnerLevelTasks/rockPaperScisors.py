print("What is your choice?")
user_choice = input().lower()
import random
possible_choices = ["rock","paper", "scissors"]
computer_choice = random.choice(possible_choices)
print(f"Computer choice: {computer_choice}")
if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win")
    else:
        print("You lose")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win")
    else:
        print("You lose")
else:
    print("Invalid input. You lose ;(")

