import random
import string


# This program will take a phrase that user wants to use so that that the program turns that simple phrase into a easy to remember complicated password

# Gets the user input of the simple phrase to turn it into a complicated password basically mutate it 
def userInput():
    print("Input a simple phrase so that the program can turn it into a complicated password")
    message = input("---> ")
    return message

def generate_password(message, length=16):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    # Ensure password has at least one uppercase letter, one lowercase letter, one digit, and one special character
    password = password[:1] + random.choice(string.ascii_uppercase) + password[1:2] + random.choice(string.digits) + password[2:3] + random.choice(string.punctuation) + password[3:]
    return password

if __name__ == "__main__":
    userInput()
    password = generate_password()
    print("Generated Password:", password)
