#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>  // Include for log10 and pow

using namespace std;

int main() {
    ifstream inputFile("/home/pandulce/char.txt");

    if (!inputFile.is_open()) {
        cerr << "There was an error opening the file!" << endl;
        return 1; // exits the program with an error code
    }

    // variables store the info from the file
    string line;
    int lineNumber = 0;
    int totalSum = 0;

    while (getline(inputFile, line)) {
        lineNumber++;

        istringstream iss(line);
        int lineSum = 0;

        int currentNumber;
        while (iss >> currentNumber) {
            if (iss.fail()) {
                cerr << "Error reading an integer from line " << lineNumber << endl;
                break;
            }

            if (currentNumber >= 10 && currentNumber <= 99) {
                // If the number is two digits, take the first and last digits
                int firstDigit = currentNumber / 10;
                int lastDigit = currentNumber % 10;
                int twoDigitNumber = firstDigit * 10 + lastDigit;

                lineSum += twoDigitNumber;
            } else if (currentNumber >= 0 && currentNumber <= 9) {
                // If the number is a single digit, repeat it to form a two-digit number
                int twoDigitNumber = currentNumber * 11;

                lineSum += twoDigitNumber;
            } else {
                // If the number has more than two digits, extract the first and last digits
                int digits = (int)log10(currentNumber);
                int firstDigit = currentNumber / pow(10, digits);
                int lastDigit = currentNumber % 10;
                int twoDigitNumber = firstDigit * 10 + lastDigit;

                lineSum += twoDigitNumber;
            }
        }

        cout << "Line " << lineNumber << " Sum: " << lineSum << endl;

        totalSum += lineSum;
    }

    cout << "Total Sum of all Lines: " << totalSum << endl;

    inputFile.close();

    return 0;
}



