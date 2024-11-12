import random

options = ["papper", "scissor", "stone"]

while True:
    user_choice = input("Enter your choice (papper, scissor, stone): ")
    if user_choice not in options:
        print("Invalid choice. Please choose from papper, scissor, or stone.")
        continue
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        print("again")
        continue
    elif (user_choice == "papper" and computer_choice == "scissor") or (user_choice == "scissor" and computer_choice == "stone") or (user_choice == "stone" and computer_choice == "papper"):
        print("You lose")
    else:
        print("You win!")

    again = input("是否繼續玩(y/n):")
    if again == "n":
        break