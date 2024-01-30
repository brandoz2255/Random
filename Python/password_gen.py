import random
import string
import hashlib


# This program will take a phrase that user wants to use so that that the program turns that simple phrase into a easy to remember complicated password

# Gets the user input of the simple phrase to turn it into a complicated password basically mutate it 


def userGreeting():
    asciiArt = """!!!!!welcome!!!!
     ____  ____  ____  ____  _      ____  ____  ____                                                 
/  __\/  _ \/ ___\/ ___\/ \  /|/  _ \/  __\/  _ \                                                
|  \/|| / \||    \|    \| |  ||| / \||  \/|| | \|                                                
|  __/| |-||\___ |\___ || |/\||| \_/||    /| |_/|                                                
\_/   \_/ \|\____/\____/\_/  \|\____/\_/\_\\____/                                                
                                                                                                 
 _____ _____ _      _____ ____  ____  _____  ____  ____                                          
/  __//  __// \  /|/  __//  __\/  _ \/__ __\/  _ \/  __\                                         
| |  _|  \  | |\ |||  \  |  \/|| / \|  / \  | / \||  \/|                                         
| |_//|  /_ | | \|||  /_ |    /| |-||  | |  | \_/||    /                                         
\____\\____\\_/  \|\____\\_/\_\\_/ \|  \_/  \____/\_/\_\                                         
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
       ____ ___  _ _____  _     ____  _        _____ ____  _____  _  _____  _  ____  _      _  _ 
      /  __\\  \///__ __\/ \ /|/  _ \/ \  /|  /  __//  _ \/__ __\/ \/__ __\/ \/  _ \/ \  /|/ \/ \
      |  \/| \  /   / \  | |_||| / \|| |\ ||  |  \  | | \|  / \  | |  / \  | || / \|| |\ ||| || |
      |  __/ / /    | |  | | ||| \_/|| | \||  |  /_ | |_/|  | |  | |  | |  | || \_/|| | \||\_/\_/
      \_/   /_/     \_/  \_/ \|\____/\_/  \|  \____\\____/  \_/  \_/  \_/  \_/\____/\_/  \|(_)(_)
                                                                                                 
    """
    print(asciiArt)


def userInput():
    print("------------------------------------------------------------------------------")
    print("\nInput a simple phrase so that the program can turn it into a complicated password\n")
    message = input("\n---> ")
    print("------------------------------------------------------------------------------")

    return message


def generate_username(message):
  # Split the phrase into words
  words = message.split()
  
  # Generate acronym from the first letters of each word
  acronym = ''.join(word[0] for word in words)
  
  # Append a random number to the acronym
  number = '{:03d}'.format(random.randrange(1, 999))
  username = acronym + number
  
  return username

def askUserEmsg():
 while True:
       print("------------------------------------------------------------------------------\n")
       ask = input("Would you like to use this program [Y/n]: ").lower()
       print(ask)
       print("\n------------------------------------------------------------------------------")

       if ask == 'y':
           return True
       elif ask == 'n':
           return False
       else:
           print("Syntax error!!")


def exitMessage():
    print("\n------------------------------------------------------------------------------\n")

    Emsg = "Thanks for using this program to create your login credentials!!" 
    print(Emsg)

    print("\n------------------------------------------------------------------------------")
   


def generate_password(message, length=16):
   # Hash the message
   hashed_message = hashlib.sha256(message.encode()).hexdigest()
   
   # Convert the hashed message to a list of characters
   hashed_chars = list(hashed_message)
   
   # Select random characters from the hashed message to form the password
   password = ''.join(random.choice(hashed_chars) for _ in range(length))

   # Ensure password has at least one uppercase letter, one lowercase letter, one digit, and one special character
   password = password[:1] + random.choice(string.ascii_uppercase) + password[1:2] + random.choice(string.digits) + password[2:3] + random.choice(string.punctuation) + password[3:]
   return password

main =  True

userGreeting()

while main:

    if __name__ == "__main__":
        message = userInput()
        password = generate_password(message)
        username = generate_username(message)
        print("\nGenerated Password:\n", password)
        print("\nGenerated Username:\n", username)

    with open('password.pass','a') as f:
        f.write('Here is the Generated Password(s) and Username(s) --> \n')
        f.write(f'Username:  {username}\n')
        f.write(f'Password:  {password}\n\n')
    
    main = askUserEmsg()


exitMessage()
