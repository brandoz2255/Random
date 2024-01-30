
# Lab 12 adding it to Lab 13 lets see how it goes dripped out one 
class TemperatureConverter:
    def __init__(self):
        pass

    def user_greeting(self):
        print("Hello welcome!")
        print("\nThis program will convert degrees Celsius to degrees Fahrenheit.")

    def ask_again(self):
        while True:
            print("\nWould you like to run this program again:")
            print("------------------------------------------")
            user_input = input("If so, please enter either [y/n]: ")
        
            if user_input == 'y':
                return True
            elif user_input == 'n':
                print("----------------------------------------")
                print("Ok then, have a nice day!")
                return False
            else:
                print("-----------------------------------------")
                print("Did not compute, please try again!")

    def convert_and_display(self):
        # Get user input and assign to a variable (float data type)
        celsius = float(input("\nPlease enter the temperature in degrees Celsius; you may use decimals: "))

        # Perform the temperature conversion and assign the result to a variable
        fahrenheit = (celsius * 9/5) + 32

        # Display the results with one decimal point
        print("\n {:.1f} degrees Celsius is equal to {:.1f} degrees Fahrenheit.".format(celsius, fahrenheit))

    def main(self):
        self.user_greeting()

        while True:
            self.convert_and_display()

            # Goes through what happens in the ask_again function to determine the status of the main program
            if not self.ask_again():
                break