# Brandon Sanchez
# 55
# 11/29/2023
# Final Lab

# This program will essentially calculate and output the Subtotal, Tax (if CA), Shipping and Handling, and Total Due

# This is the function that displays the user greeting 

# Also please don't take off points for my decorations I had fun with this!! 

def user_greeting():
    print("""
                                                     ,--,              ,--,                                ,---,    ,---,  
                           ,--.               ,---.'|           ,---.'|                             ,`--.' | ,`--.' |  
    ,---,.   ,---,       ,--.'|   ,---,       |   | :           |   | :      ,---,           ,---,. |   :  : |   :  :  
  ,'  .' |,`--.' |   ,--,:  : |  '  .' \      :   : |           :   : |     '  .' \        ,'  .'  \'   '  ; '   '  ;  
,---.'   ||   :  :,`--.'`|  ' : /  ;    '.    |   ' :           |   ' :    /  ;    '.    ,---.' .' ||   |  | |   |  |  
|   |   .':   |  '|   :  :  | |:  :       \   ;   ; '           ;   ; '   :  :       \   |   |  |: |'   :  ; '   :  ;  
:   :  :  |   :  |:   |   \ | ::  |   /\   \  '   | |__         '   | |__ :  |   /\   \  :   :  :  /|   |  ' |   |  '  
:   |  |-,'   '  ;|   : '  '; ||  :  ' ;.   : |   | :.'|        |   | :.'||  :  ' ;.   : :   |    ; '   :  | '   :  |  
|   :  ;/||   |  |'   ' ;.    ;|  |  ;/  \   \'   :    ;        '   :    ;|  |  ;/  \   \|   :     \;   |  ; ;   |  ;  
|   |   .''   :  ;|   | | \   |'  :  | \  \ ,'|   |  ./         |   |  ./ '  :  | \  \ ,'|   |   . |`---'. | `---'. |  
'   :  '  |   |  ''   : |  ; .'|  |  '  '--'  ;   : ;           ;   : ;   |  |  '  '--'  '   :  '; | `--..`;  `--..`;  
|   |  |  '   :  ||   | '`--'  |  :  :        |   ,/            |   ,/    |  :  :        |   |  | ; .--,_    .--,_     
|   :  \  ;   |.' '   : |      |  | ,'        '---'             '---'     |  | ,'        |   :   /  |    |`. |    |`.  
|   | ,'  '---'   ;   |.'      `--''                                      `--''          |   | ,'   `-- -`, ;`-- -`, ; 
`----'            '---'                                                                  `----'       '---`"   '---`"  
                                                                                                                       
    \n""")
    print("---------------------------------------------------------------------------------")
    print("Hello! and welcome to my progam!")
    print("This Program will essentially calculate the output and subtotal tax if its CA")
    print(", and the total due")
    print("---------------------------------------------------------------------------------")

def stateAbbreviation():
    abbreviations = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]
    while True:
        # User input for state abbreviation
        user_input = input("\nPlease input one of the 50 states (Format: abbreviations or 'ls' for list): ").upper()
        print("---------------------------------------------------------------------------------")

        # Check if user entered 'ls' to list states
        if user_input == "LS":
            print("\nList of states:\n")
            print(abbreviations)
            print("---------------------------------------------------------------------------------")


        # Check if user entered a valid state abbreviation
        elif user_input in abbreviations:
            # Special handling for California (CA) with tax rate
            if user_input == "CA":
                tax_rate = 0.08
                print(f"\nThe following tax rate will be added onto the total amount: {tax_rate}\n")
                print("---------------------------------------------------------------------------------")


            # Return the variable that contains the state abbreviation
            return user_input

        # If user input is not 'ls' or a valid state abbreviation, display an error message
        else:
            print("\nNot valid! Syntax error!!\n")

# Gets the function for getting the product information
def productInfo():
    # This is the product list
    product_list = []

    # Controls the loop
    loop_info = True

    while loop_info:
        # gets the input for the item quantity
        print("---------------------------------------------------------------------------------")
        print("\nIf you are done type [0]\n")
        itemQuantity = float(input("\nPlease enter the Item quantity: \n"))
        print("---------------------------------------------------------------------------------")
        print(itemQuantity)
        print("---------------------------------------------------------------------------------")

        if itemQuantity == 0:
            # change the variable so the loop exits 
            break
        else:
            # Changes the variable to exit the loop
            itemWeight = float(input("\nPlease enter the Item weight: \n"))
            itemCost = float(input("\nPlease enter the Item Cost: \n"))

            # Append a tuple with itemQuantity, itemWeight, and itemCost to the product_list
            product_list.append((itemQuantity, itemWeight, itemCost))

    return product_list

# This is the function for the calculations
def calculations(product_info):
    box_weight = 0
    sub_total = 0

    # Iterate through the product information
    for main_index in range(len(product_info)):
        item_quantity, item_weight, item_cost = product_info[main_index]

        box_weight += item_quantity * item_weight
        sub_total += item_quantity * item_cost

    # Calculate the shipping
    shipping = box_weight * 0.25

    # Determine handling cost based on box weight
    if box_weight < 10:
        handling = 1
    elif box_weight > 100:
        handling = 5
    else:
        handling = 3

    # Add shipping and handling costs together
    total_shipping_handling = shipping + handling

    # Return subtotal, shipping, and handling
    return sub_total, total_shipping_handling

def userOption():
    print("---------------------------------------------------------------------------------")
    print("\nWould you like to use this program again [y/n]\n")
    input_option = input("-->: ").lower()
    print(input_option)
    print("---------------------------------------------------------------------------------")

    while input_option != 'y' and input_option != 'n':
        print("Did not understand. Please enter either y/n")
        input_option = input("-->: ").lower()

    if input_option == 'y':
        return True
    elif input_option == 'n':
        print("""\n /$$$$$$                            /$$ /$$                           /$$ /$$
 /$$__ $$                          | $$| $$                          | $$| $$
| $$ \__/ /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$ /$$   /$$ /$$$$$$ | $$| $$
| $$ /$$$$ /$$__ $$ /$$__ $$ /$$__ $$| $$__ $$| $$ | $$ /$$__ $$| $$| $$
| $$|_ $$| $$ \ $$| $$ \ $$| $$ | $$| $$ \ $$| $$ | $$| $$$$$$$$| $$| $$
| $$ \ $$| $$ | $$| $$ | $$| $$ | $$| $$ | $$| $$ | $$| $$_____/| $$| $$
| $$$$$$/| $$$$$$/| $$$$$$/| $$$$$$$| $$$$$$$/| $$$$$$$| $$$$$$$ /$$ /$$
 \______/ \______/ \______/ \_______/|_______/ \____ $$ \_______/|__/|__/
                                                   /$$ | $$                  
                                                 | $$$$$$/                  
                                                   \______/                   """)

    return False



         




# -----------------MAIN----------------------------------

# Controla the main loop of the progam
mainProgram = True

# The loop for the main progam
while mainProgram == True:

    # Calls the user greeting function
    user_greeting()

    # calls the stateabbreviation function
    state = stateAbbreviation()

    # calls the product information function 
    getProductInfo = productInfo()

    # calls and calculates the function 
    subtotal, shipping_handling = calculations(getProductInfo)

    if state == 'CA':
        tax = subtotal * 0.08
    else:
        tax = 0.00

    the_total = subtotal + tax + shipping_handling

    print("---------------------------------------------------------------------------------")
    print(format('Subtotal:', '<25'), format(subtotal, '>10,.2f'))
    print(format('Tax:', '<25'), format(tax, '>10,.2f'))
    print(format('Shipping and Handling:', '<25'), format(shipping_handling, '>10,.2f'))
    print(format('Total:', '<25'), format(the_total, '>10,.2f'))
    print("---------------------------------------------------------------------------------")


    mainProgram = userOption()

