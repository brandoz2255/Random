#include <iostream>
#include <string>
#include <unistd.h>

int main() {
    std::string rotatingBar = "/-\\|";
    int rotatingIndex = 0;

    while (true) {
        std::cout << "\r" << rotatingBar[rotatingIndex];
        rotatingIndex = (rotatingIndex + 1) % rotatingBar.size();
        usleep(100000); // sleep for 100 milliseconds
    }

    return 0;
}
