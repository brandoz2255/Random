#include <iostream>
#include <iomanip>
#include "temperature_converter.h"

class TemperatureConverter{
    // ok the public statement tells C++ that functions outside the public namespace can use what is inside of the namespace
    public:
    void user_greeting(){
        std::cout << "Hello! and welcome to this program!";
        std::cout << "\nThis Program will convert Celsuis to degrees Fahrenheit\n";
    }
    // Since we are asking to return a true a false we use thje boolean data type
    bool askAgain(){
        while (true){
            std::cout << "\nWould you like to run this program again:\n";
            std::cout << "-------------------------------------------";
            char  userInput;
            std::cout << "\nif so either enter a [Y/N]: ";
            std::cin >> userInput; 

            if (userInput == 'y' || userInput == 'Y'){
                return true;
            } else if (userInput == 'n' || userInput == 'N'){
                std::cout << "-------------------------------------------";
                std::cout << "\nok then have a nice day!\n";
                return false;
            } else {
                std::cout << "-------------------------------------------";
                std::cout << "\nDid not compute, please try again\n";
            }
        }

    }

    void convertAndDisplay(){
        // Get user input and assign to a variable (Float data type)
        double celsius;
        std::cout << "\nPlease enter the temperature in degrees celsius:  ";
        std::cin >> celsius; 

        // Performs the temperature in degrees celsius and assigns the result to the decimal point
        double fahrenheit = (celsius * 9/5)+32;

        //Displays the results of the math 
        std::cout << "\n" << std::fixed << std::setprecision(1) << celsius
                  << "\ndegrees Celsius is equal to\n" << fahrenheit << "\ndegrees farenheit.\n";
    }

    void main(){
        user_greeting();

        while (true){
            convertAndDisplay();

            //goes through what happens in the askAgain function
            if (!askAgain()){
                break;
            }
        }
    }
};

// Main  function where all the code happens the main part of the code
// in which the other functions are the C++ versions of the def functions 
int main(){
    TemperatureConverter temperatureConverter;
    temperatureConverter.main();
    return 0;
    
}