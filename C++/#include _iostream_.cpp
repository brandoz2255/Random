#include <cstdio>

enum class Race {
    Dinan,
    Teklyn,
    Ivyn,
    Moiran,
    Camite,
    Julian,
    Aidan,
};

int main() {
    Race race = Race::Dinan;

    switch (race) {
    case Race::Dinan:
        printf("You work hard sir!");
        break;

    case Race::Teklyn:
        printf("You are very strong");
        break;

    case Race::Ivyn:
        printf("You are a great leader!");
        break;

    case Race::Moiran:
        printf("My, how versatile you are!");
        break;

    case Race::Camite:
        printf("You're incredibly helpful!");
        break;

    case Race::Julian:
        printf("Anything you want!");
        break;

    case Race::Aidan:
        printf("Wow, what a sigma!");
        break;

    default:
        printf("Error: Unknown race!");
    }

    return 0;
}
