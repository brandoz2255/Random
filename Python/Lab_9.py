
# Brandon Sanchez
#55
# 10/22/2023
#Lab 8



#This program will do conversions in multiple fields and will work both ways
#Creates the user greeting 
print("Hello this program will convert ounces to grams, inches to centimeters, and kilometers to miles and the process will work both ways")


# This variable is the main loop 
main_loop='y'

#The Main loop of my code 
while main_loop =='y':
    #is asking the users input to begin the conversion
    message = input("""
    Please input the following to use this program for conversion. 
    'I' Will convert Inches to Centemeters.
    'C' Will convert Centimeters to Inches.
    'O' Will convert Ounces to Grams. 
    'G' Will convert from Grams to Ounces
    'M' Will convert from Miles to Kilometers 
    'K' Will convert Kilometers to miles 
    Type here: """).lower()

    #Asks the user for the value needed to do the conversion
    number_1 = float(input("\n Please enter an integer: "))

    #Does the conversions
    if message == 'i':
        in_to_Cent = number_1 * 2.54
        print(f"\n{number_1} Equals: {in_to_Cent:,.2f} Centemeters")
    elif message == 'c':
        cent_to_In = number_1 * 0.3937
        print(f"\n{number_1} Euquals: {cent_to_In:,.2f} Inches")
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

    # This is the Error Loop to make sure the user inputs the correct option
    while message not in ['i', 'c', 'o', 'g', 'm','k']:
        message = input("""\n
        Im sorry I did not Understand the value please type the correct value:
        Please input the following to use this program for conversion. 
        'I' Will convert Inches to Centemeters.
        'C' Will convert Centimeters to Inches.
        'O' Will convert Ounces to Grams. 
        'G' Will convert from Grams to Ounces
        'M' Will convert from Miles to Kilometers 
        'K' Will convert Kilometers to miles 
        Type here: """).lower()



    #@Error messasge for reusing the program
    main_loop = input("\nThanks for using my program. Would you like to use this program again [Y/N]: ").lower()

while main_loop not in ['y', 'n']:
    main_loop = input("\nI did not understand your value. Please enter 'Y' to continue or 'N' to exit: ").lower()

#prints an exit message
print("\nthanks for using my program!!")








