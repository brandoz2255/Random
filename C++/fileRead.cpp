#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    ifstream inputFIle("/home/pandulce/char.txt");

    if(!inputFIle.is_open()){
        cerr << "There was an error opening the file!" << endl;
        return 1; //exits the program with an error code
    }

    // variablels store the info from the file
    string line;
    int lineNumber = 0;
    int totalSum = 0;

    while (getline(inputFIle, line)){
        lineNumber++;

        istringstream iss(line);
        int currentNumber;
        int lineSum = 0;

        // Modify this to solve the challenge 
        while (iss >> currentNumber){
            if (iss.fail()){
                cerr << "error!" << lineNumber << endl;
                break;
            }
            if(currentNumber >=10 && currentNumber <=99){
                // Looks at the first digits 
                int firstDigit = currentNumber /10;
                //Looks at the last digits 
                int lastDigit = currentNumber %10;
                //combines the first and last digits to make a two digit number 
                // howe can we add a way to make the lines that contain one digit numbers into a two digits number
                //for example if a line has aklf4jskldfj we would take that 4 turn it into 44 etc  
                int twoDigitNumber = firstDigit * 10 + lastDigit;


                lineSum += twoDigitNumber;
                

            }else {
                cerr << "invalid" << lineNumber << ": " << currentNumber << endl;

            }
            
        }

        cout << "Line " << lineNumber << " Sum: " << lineSum << endl;

        totalSum += lineSum; 

    }

    cout << "Total Sum of all Lines: " << totalSum << endl;

    inputFIle.close();

    return 0;
}
