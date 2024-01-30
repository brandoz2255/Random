#include <iostream>
#include <cstdlib>
#include <thread>
#include <chrono>

void clear_screen() {
    system("cls");
}

void animate_text() {
    std::string text = "Hello, World!";
    
    for (size_t i = 0; i < text.length(); ++i) {
        clear_screen();
        std::cout << text.substr(0, i + 1) << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
    }
}

void countdown_timer(int seconds) {
    for (int i = seconds; i > 0; --i) {
        clear_screen();
        std::cout << "Time left: " << i << " seconds" << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    clear_screen();
    std::cout << "Time's up!" << std::endl;
}

void loading_spinner() {
    const std::string spinner = "|/-\\";
    for (int i = 0; i < 10; ++i) {
        for (char ch : spinner) {
            clear_screen();
            std::cout << "Loading... " << ch << std::flush;
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
    }
}

int main() {
    animate_text();

    std::this_thread::sleep_for(std::chrono::seconds(1)); // Wait for 1 second

    countdown_timer(5);

    std::this_thread::sleep_for(std::chrono::seconds(1)); // Wait for 1 second

    loading_spinner();

    return 0;
}
