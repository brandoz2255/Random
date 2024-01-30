#include <iostream>
#include <iomanip>
#include <limits>

enum ConversionType {
    InchesToCentimeters,
    CentimetersToInches,
    OuncesToGrams,
    GramsToOunces,
    MilesToKilometers,
    KilometersToMiles,
    CelsiusToFahrenheit
};

// Function for the user greeting. Nothing in, nothing out.
void userGreeting() {
    std::cout << "\033[1;32m"
              << R"(
   .____       _____ __________   ____________   ._._. 
|    |     /  _  \\______   \ /_   \_____  \  | | | 
|    |    /  /_\  \|    |  _/  |   | _(__  <  | | | 
|    |___/    |    \    |   \  |   |/       \  \|\| 
|_______ \____|__  /______  /  |___/______  /  ____ 
        \/       \/       \/              \/   \/\/ 
    )" << "\033[0m" << std::endl;

    std::cout << "Hello and welcome to this program!" << std::endl;
    std::cout << "\033[1;32m---------------------------------------------------\033[0m" << std::endl;
    std::cout << "\033[1;93mEssentially, this program will allow you to do conversions in multiple fields\033[1;32m"
              << std::endl;
    std::cout << "---------------------------------------------------" << std::endl;
}

// Function to get the conversion type and error check it. Returns the converted type.
ConversionType getConversionType() {
    std::string message;
    std::cout << "\033[1;32mPlease input the following to use this program for conversion.\033[0m" << std::endl;
    std::cout << "\033[1;32m'I' Will convert Inches to Centimeters.\033[0m" << std::endl;
    std::cout << "\033[1;32m'C' Will convert Centimeters to Inches.\033[0m" << std::endl;
    std::cout << "\033[1;32m'O' Will convert Ounces to Grams.\033[0m" << std::endl;
    std::cout << "\033[1;32m'G' Will convert from Grams to Ounces.\033[0m" << std::endl;
    std::cout << "\033[1;32m'M' Will convert from Miles to Kilometers.\033[0m" << std::endl;
    std::cout << "\033[1;32m'K' Will convert Kilometers to miles.\033[0m" << std::endl;
    std::cout << "\033[1;32m'T' Will convert Celsius to Fahrenheit.\033[0m" << std::endl;
    std::cout << "Type here: ";
    std::cin >> message;

    if (message == "I" || message == "i") {
        return InchesToCentimeters;
    } else if (message == "C" || message == "c") {
        return CentimetersToInches;
    } else if (message == "O" || message == "o") {
        return OuncesToGrams;
    } else if (message == "G" || message == "g") {
        return GramsToOunces;
    } else if (message == "M" || message == "m") {
        return MilesToKilometers;
    } else if (message == "K" || message == "k") {
        return KilometersToMiles;
    } else if (message == "T" || message == "t") {
        return CelsiusToFahrenheit;
    }

    std::cout << "\033[1;32m---------------------------------------------------\033[0m" << std::endl;
    std::cout << "I'm sorry, I did not understand the value. Please type the correct value." << std::endl;
    return static_cast<ConversionType>(-1);
}

// Function to get user input and perform the conversion. Prints the result.
void calculateAndDisplay(ConversionType conversionType) {
    double math; // sets the variable so that it can be used in C++ Compiler 

    if (conversionType == CelsiusToFahrenheit) {
        // Implement the Celsius to Fahrenheit conversion here
    } else {
        std::cout << "\033[1;36m---------------------------------------------------\033[0m" << std::endl;
        double number;
        std::cout << "\nPlease enter an integer: ";
        std::cin >> number;

        switch (conversionType) {
            case InchesToCentimeters:
                // Implement the Inches to Centimeters conversion here
                math = number * 2.54;
                std::cout << "\n" << number << "\nInches  Equals\n" << math << "\nCentimeters" << std::endl;
                break;
            case CentimetersToInches:
                // Implement the Centimeters to Inches conversion here
                math = number * 0.3937;
                std::cout << "\n" << number << "\nCentimeters  Equals\n" << math << "\nInches" << std::endl;
                break;
            case OuncesToGrams:
                // Implement the Ounces to Grams conversion here
                math = number  * 28.34952;
                std::cout << "\n" << number << "\nOunces  Equals\n" << math << "\nGrams" << std::endl;
                break;
            case GramsToOunces:
                // Implement the Grams to Ounces conversion here
                math = number / 28.34952;
                std::cout << "\n" << number << "\nGrams  Equals\n" << math << "\nOunces" << std::endl;
                break;
            case MilesToKilometers:
                // Implement the Miles to Kilometers conversion here
                math = number * 1.609344;
                std::cout << "\n" << number << "\nMiles  Equals\n" << math << "\nKilometers" << std::endl;
                break;
            case KilometersToMiles:
                // Implement the Kilometers to Miles conversion here
                math = number * 0.621371;
                std::cout << "\n" << number << "\nKilometers  Equals\n" << math << "\nMiles" << std::endl;
                break;
            default:
                std::cerr << "\033[1;31mInvalid conversion type\033[0m" << std::endl;
                return;
        }

        std::cout << "\033[1;36m---------------------------------------------------\033[0m" << std::endl;
    }
}

// Function to ask the user if they want to continue. Returns True or False.
bool askToContinue() {
    std::cout << "\033[1;32m---------------------------------------------------\033[0m" << std::endl;

    char answer;
    std::cout << d
    std::cin >> answer;

    if (answer == 'Y' || answer == 'y') {
        return true;
    } else if (answer == 'N' || answer == 'n') {
        std::cout << "\033[1;32m-----------------------OK--------------------------\033[0m" << std::endl;
        std::cout << "\033[1;32m---------------------------------------------------\033[0m" << std::endl;
        return false;
    } else {
        std::cout << "\033[1;32m---------------------------------------------------\033[0m" << std::endl;
        return false;
    }
}

// Function for the user exit option. Nothing in, nothing out.
void exitMessage() {
    std::cout << "\033[1;34m---------------------------------------------------\033[0m" << std::endl;
    std::cout << "\033[1;34m---------thanks for using my program!!-----------\033[0m" << std::endl;
    std::cout << "\033[1;34m---------------------------------------------------\033[0m" << std::endl;
}

// Main section of the code
int main() {
    // Main program variable
    bool runMainProgram = true;

    // Main program loop
    while (runMainProgram) {
        // Greet the user
        userGreeting();

        // Get conversion type
        ConversionType conversionTypeMain = getConversionType();
        if (conversionTypeMain != static_cast<ConversionType>(-1)) {
            // Calculate and display result
            calculateAndDisplay(conversionTypeMain);

            // Ask user to continue
            runMainProgram = askToContinue();
        }
    }

    // Exit message
    exitMessage();

    return 0;
}
