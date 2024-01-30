
import time

def intro():
    print("Welcome to 'Post-Apocalyptic Adventure'!")
    time.sleep(1)
    print("The world has ended, and you're one of the survivors.")
    time.sleep(1)
    print("Your goal is to find a safe haven.")
    time.sleep(1)

def make_choice_1(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and", len(options))
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    intro()

    # Start of the game
    choice = make_choice_1("You wake up in a ruined building. What do you do?", ["Search for supplies.", "Leave the building."])

    if choice == 1:
        print("You find some food and a first-aid kit. Your journey continues.")
    else:
        print("You cautiously exit the building and begin your adventure.")

    # More game choices can be added here
    # Example: choice = make_choice("You find a fork in the road. Which way do you go?", ["Left.", "Right."])

    print("Congratulations! You've survived the post-apocalyptic adventure.")

if __name__ == "__main__":
    play_game()
