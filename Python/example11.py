# Brandon Sanchez
# 55
# 11/8/2023
# Lab 11

# Program Description: This program allows the user to enter a state name and displays its abbreviation, or vice versa.

# This is responsible for the list of states
state_list = ["ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "NEW MEXICO", 
"WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING"]
state_abbreviations = ["AL", "AK", "AZ", "AR", "CA", "NM", "WA", "WV", "WI", "WY"]

# Responsible for the user greeting 
print("Welcome to the State Lookup Program!")

# Variable to control the user input loop
input_loop = True

# Main program loop
while input_loop:
    
    # Get the input for which way the program should run
    user_input = input("Please type 'ab' to input a state abbreviation or 'as' to input a state name: ")
    
    # Error check for this input
    if user_input not in ['ab', 'as']:
        print("\nInvalid input. Please enter 'ab' for abbreviation or 'as' for state name.")
        continue

    # Set up the input line and pick the list for error checking of the state name or abbreviation
    if user_input == 'as':
        input_value = input("\nEnter the state name: ").upper()
        state_lookup_list = state_list
        lookup_type = "abbreviation"
    else:
        input_value = input("\nEnter the state abbreviation: ").upper()
        state_lookup_list = state_abbreviations
        lookup_type = "name"

    # Error check for this input
    if input_value not in state_lookup_list:
        print(f"\n{lookup_type.upper()} '{input_value}' not found.")
    else:
        # Iterate through the correct list to find the name or abbreviation entered
        found = False
        for index, item in enumerate(state_lookup_list):
            if input_value == item:
                found = True
                if user_input == 'as':
                    print(f"\nThe state name is {state_abbreviations[index]}.")
                else:
                    print(f"\nIt's the abbreviation for state {state_list[index]}.")
        
        if not found:
            print(f"\n{lookup_type.upper()} '{input_value}' not found.")

    # Ask the user if they want to run the program again
    run_again = input("\nDo you want to look up another state? (Enter 'yes' or 'no'): ").lower()
    
    # Error check for this input
    if run_again != 'yes':
        input_loop = False

# Exit message
print("Thank you for using the State Lookup Program. Goodbye!")

