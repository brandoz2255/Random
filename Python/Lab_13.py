# Brandon Sanchez
# 55
# 11/24/2023
# Lab 13

# This program will do conversions in multiple fields and will work both ways

# Function for the user greeting creates the user greeting
def user_greeting():
    print("Hello and welcome to this program!")
    print("---------------------------------------------------")
    print("Essentially this program will allow you to do conversions in multiple fields")

# The user input function
def user_option():
    message = input("""
    Please input the following to use this program for conversion. 
    'I' Will convert Inches to Centimeters.
    'C' Will convert Centimeters to Inches.
    'O' Will convert Ounces to Grams. 
    'G' Will convert from Grams to Ounces
    'M' Will convert from Miles to Kilometers 
    'K' Will convert Kilometers to miles 
    Type here: """).lower()

    # Error checks the user input
    if message in ['i', 'c', 'o', 'g', 'm', 'k']:
        return message
    
    print("---------------------------------------------------")
    print("I'm sorry, I did not understand the value. Please type the correct value.")
    return None

# Function for the user input
def user_input(message):
    print("---------------------------------------------------")
    number_1 = float(input("\n Please enter an integer: "))

    # Does the conversions
    if message == 'i':
        in_to_Cent = number_1 * 2.54
        print(f"\n{number_1} Equals: {in_to_Cent:,.2f} Centimeters")
    elif message == 'c':
        cent_to_In = number_1 * 0.3937
        print(f"\n{number_1} Equals: {cent_to_In:,.2f} Inches")
    elif message == 'o':
        ounces_to_grams = number_1 * 28.34952
        print(f"\n{number_1} Equals: {ounces_to_grams:,.2f} Grams")
    elif message == 'g':
        grams_to_ounces = number_1 / 28.34952
        print(f"\n{number_1} Equals: {grams_to_ounces:,.2f} Ounces")
    elif message == 'm':
        miles_to_kilo = number_1 * 1.609344
        print(f"\n{number_1} Equals: {miles_to_kilo:,.2f} Kilometers")
    elif message == 'k':
        kilos_to_miles = number_1 * 0.621371
        print(f"\n{number_1} Equals: {kilos_to_miles:,.2f} Miles")

# Asks the user if they would like to run the program
def use_again():
    print("---------------------------------------------------")
    answer = input("Would you like to use this program again [Y/N]: ").upper()
    if answer == 'Y':
        return True
    elif answer == 'N':
        print("---------------------------------------------------")
        print("-----------------------OK--------------------------")
        return False
    else:
        return False

# Function for the user exit message
def exit_message():
    print("---------------------------------------------------")
    print("\n---------thanks for using my program!!-----------")
    print("---------------------------------------------------")
    
# Main section of the code    
user_greeting()

# Main program variable
main_program = True

# Main program loop
while main_program:
    option = user_option()
    if option is not None:
        print("---------------------------------------------------")
        print(f"You have chosen option {option}")
        print("---------------------------------------------------")
        user_input(option)
        main_program = use_again()


# Prints the exit message
exit_message()
