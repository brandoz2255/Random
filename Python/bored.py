def main():
    print("Welcome to the Interactive Story!")

    name = input("What's your name? ")
    print(f"Hello, {name}! Let's begin the story.")

    # Part 1
    print("\nPart 1: The Mysterious Forest")
    print("You find yourself in a mysterious forest.")
    choice1 = input("Do you want to go 'left' or 'right'? ").lower()

    if choice1 == 'left':
        print("You discover a hidden path.")
    elif choice1 == 'right':
        print("You encounter a strange creature.")
    else:
        print("Invalid choice. The story takes an unexpected turn.")

    # Part 2
    print("\nPart 2: The Hidden Path")
    print("You follow the hidden path and arrive at a magical lake.")
    choice2 = input("Do you want to 'swim' in the lake or 'skip' stones? ").lower()

    if choice2 == 'swim':
        print("You discover an underwater cave.")
    elif choice2 == 'skip':
        print("A magical portal opens.")
    else:
        print("Invalid choice. The story takes an unexpected turn.")

    # Part 3
    print("\nPart 3: The Discovery")
    print("You explore further and make a discovery.")
    choice3 = input("Do you want to 'keep' the discovery or 'return' home? ").lower()

    if choice3 == 'keep':
        print("You unlock the secrets of the magical forest.")
        print("Congratulations, you've completed the story!")
    elif choice3 == 'return':
        print("You decide to return home.")
        print("The adventure ends for now.")
    else:
        print("Invalid choice. The story takes an unexpected turn.")

    print("Thank you for playing the Interactive Story!")

if __name__ == "__main__":
    main()

