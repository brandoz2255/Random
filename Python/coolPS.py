import random
import string
import hashlib
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def userGreeting():
    asciiArt = f"""{Fore.BLUE}!!!!!welcome!!!!
     {Fore.YELLOW} ____  ____  ____  ____  _      ____  ____  ____                                                 
/  __\/  _ \/ ___\/ ___\/ \  /|/  _ \/  __\/  _ \\                                                
|  \/|| / \\||    \|    \| |  ||| / \\||  \/|| | \\|                                                
|  __/| |-||\___ |\___ || |/\||| \\_/||    /| |_/{Style.RESET_ALL}                                                
\\_/   \\_/ \\|\\____/\\____/\\_/  \\|\\____/\\_/\\\\\\____/                                                
                                                                                                 
 {Fore.GREEN}_____ _____ _      _____ ____  ____  _____  ____  ____                                          
/  __//  __// \\  /|/  __//  __\\/  _ \\/__ __\\/  _ \\/  __\\                                         
| |  _|  \\  | |\\ |||  \\  |  \\/|| / \\|  / \\  | / \\||  \\/|                                         
| |_//|  /_ | | \\|||  /_ |    /| |-||  | |  | \\_/||    /                                         
\\____\\\\____\\\\_/  \\|\\____\\\\_/\\_/\\\\_/ \\|  \\_/  \\____/\\_/\\_\\                                         
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
       ____ ___  _ _____  _     ____  _        _____ ____  _____  _  _____  _  ____  _      _  _ 
      /  __\\{Fore.RED} \\{/Fore.YELLOW}///__ __\\/ \\ /|/  _ \\/ \\  /|  /  __/{Fore.RED}/  _ \\/__ __\\/ \\/__ __\\/ \\/  _ \\/ \\  /|/ \\/ \\
      |  \\/| \\/  {Fore.RED}/   / \\  | |\\/||| / \\|| |\ ||  |  \\/| | \\  {Fore.YELLOW}| / \\  | |  / \\  | || / \\|| |\\ ||| || |
      |  __/ / /    | |  | | ||| \\_/|| | \\||  |  /_ | |_/|  | |  | |  | |  | || \\_/|| | \\||\\_/\\_/
      \\_/   /_/     \\_/  \\_/ \\|\\____/\\_/  \\|  \\____\\\\____/  \\_/  \\_/  \\_/  \\_/\\____/\\_/  \\|({Style.RESET_ALL})({Style.RESET_ALL})
                                                                                                 
    """
    print(asciiArt)

def colored_input(prompt):
    return input(f"{Fore.CYAN}{prompt}{Style.RESET_ALL}")

def colored_output(message, color=Fore.WHITE):
    print(f"{color}{message}{Style.RESET_ALL}")

def userInput():
    colored_output("------------------------------------------------------------------------------", Fore.MAGENTA)
    colored_output("\nInput a simple phrase so that the program can turn it into a complicated password\n", Fore.MAGENTA)
    message = colored_input("\n---> ")
    colored_output("------------------------------------------------------------------------------", Fore.MAGENTA)
    return message

def colored_ask_user():
    while True:
        colored_output("------------------------------------------------------------------------------\n", Fore.MAGENTA)
        ask = colored_input("Would you like to use this program [Y/n]: ").lower()
        colored_output(ask, Fore.MAGENTA)
        colored_output("\n------------------------------------------------------------------------------", Fore.MAGENTA)

        if ask == 'y':
            return True
        elif ask == 'n':
            return False
        else:
            colored_output("Syntax error!!", Fore.RED)

def exitMessage():
    colored_output("\n------------------------------------------------------------------------------\n", Fore.MAGENTA)
    Emsg = "Thanks for using this program to create your login credentials!!"
    colored_output(Emsg, Fore.GREEN)
    colored_output("\n------------------------------------------------------------------------------", Fore.MAGENTA)

def generate_password(message, length=16):
    # Hash the message
    hashed_message = hashlib.sha256(message.encode()).hexdigest()

    # Convert the hashed message to a list of characters
    hashed_chars = list(hashed_message)

    # Select random characters from the hashed message to form the password
    password = ''.join(random.choice(hashed_chars) for _ in range(length))

    # Ensure password has at least one uppercase letter, one lowercase letter, one digit, and one special character
    password = password[:1] + random.choice(string.ascii_uppercase) + password[1:2] + random.choice(
        string.digits) + password[2:3] + random.choice(string.punctuation) + password[3:]
    return password

main = True

userGreeting()

while main:
    if __name__ == "__main__":
        message = userInput()
        password = generate_password(message)
        username = generate_username(message)
        colored_output("\nGenerated Password:\n", Fore.CYAN)
        colored_output(password, Fore.YELLOW)
        colored_output("\nGenerated Username:\n", Fore.CYAN)
        colored_output(username, Fore.YELLOW)

    with open('password.pass', 'a') as f:
        f.write('Here is the Generated Password(s) and Username(s) --> \n')
        f.write(f'Username:  {username}\n')
        f.write(f'Password:  {password}\n\n')

    main = colored_ask_user()

exitMessage()

