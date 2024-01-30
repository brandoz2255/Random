from colorama import Fore, Style, init
from temp import TemperatureConverter 
import random

def user_greeting():
    message = Fore.GREEN + Style.BRIGHT + r"""Welcome to this Chatbot App it would just simply converse with you and stuff have fun!!!
    
    
    _________   ___ ___    __________________________ ___________________._._.
\_   ___ \ /   |   \  /  _  \__    ___/\______   \\_____  \__    ___/| | |
/    \  \//    ~    \/  /_\  \|    |    |    |  _/ /   |   \|    |   | | |
\     \___\    Y    /    |    \    |    |    |   \/    |    \    |    \|\|
 \______  /\___|_  /\____|__  /____|    |______  /\_______  /____|    ____
        \/       \/         \/                 \/         \/          \/\/
                                                                          
                                                                          
   ______   ______   ______   ______   ______   ______   ______           
  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/           
                                                                          
                                                                          
             ._.                              ._.                         
             | |                              | |                         
             |_|   ______            ______   |_|                         
             |-|  /_____/           /_____/   |-|                         
             | |            ______            | |                         
             |_|           /_____/            |_|                         
      __ __________          __  .__                    __                
     / / \______   \___.__._/  |_|  |__   ____   ____   \ \               
    / /   |     ___<   |  |\   __\  |  \ /  _ \ /    \   \ \              
    \ \   |    |    \___  | |  | |   Y  (  <_> )   |  \  / /              
     \_\  |____|    / ____| |__| |___|  /\____/|___|  / /_/               
                    \/                \/            \/                    
      __            .___.__  __  .__                __                    
     / /   ____   __| _/|__|/  |_|__| ____   ____   \ \                   
    / /  _/ __ \ / __ | |  \   __\  |/  _ \ /    \   \ \                  
    \ \  \  ___// /_/ | |  ||  | |  (  <_> )   |  \  / /                  
     \_\  \___  >____ | |__||__| |__|\____/|___|  / /_/                   
              \/     \/                         \/                        
    
    
    
    
    
    
    
    
    """ + Fore.WHITE + Style.BRIGHT

    print(message)

def simple_chatbot(user_input):
    greetings = [Fore.GREEN +"hello", "hi", "hey", "greetings","whats up","hola" + Fore.GREEN]
    conversation = [Fore.GREEN + "how is it going", "whats happening", " what can you do"]
    interaction = [Fore.LIGHTBLACK_EX + "what can you do", "what are you", "where have you been", "why  can't you think on your own" + Fore.CYAN]
    farewells = [Fore.GREEN+ "bye", "goodbye", "see you", "farewell"+ Fore.GREEN]
    default_responses = [Fore.GREEN +"I'm a simple chatbot. I didn't understand that.",
                         "Can you please rephrase that?",
                         "I'm still learning!" , "Bruh you know I can't understand that!!"+ Fore.GREEN]

    user_input = user_input.lower()

    if any(word in user_input for word in greetings):
        return random.choice([ Fore.GREEN + "Hello! How can I help you today?", "Hi there!", "Greetings!"])
    elif any(word in user_input for word in conversation):
        return random.choice([Fore.CYAN+"just a dark and empty void", "a simple chatbot can't do much duhh silly!","i dont know what you  mean but im glad to be talking to you" + Fore.GREEN])
    elif any(word in user_input for word in farewells):
        return random.choice([Fore.GREEN + "Goodbye! Have a great day.", "See you later!", "Farewell!"+ Fore.GREEN])
    else:
        return random.choice(default_responses)

# Main loop for interacting with the chatbot

user_greeting()

while True:
    user_input = input(Fore.BLUE + "You: " + Fore.BLUE)
    if user_input.lower() == 'exit':
        print(Fore.GREEN + "Chatbot: Goodbye!"+ Fore.GREEN)
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)

