#include<iostream>
#include<string>

using namespace std;

enum class Features{
    challenges
}

class App_Features{
    void userGreeting(){
        cout << "-----------------------------------------------------------------------------------------------------"<< endl;
        cout << "Hello! Welcome to this simple application that essentially is just for me to practice programming!" << endl;
        cout << "Nothing really specific in this App will update this when I add some cool features to this for now we are just"<< endl;
        cout << "using this to practice will the challenges from our book and our personal ideas for this app"
        cout << "-----------------------------------------------------------------------------------------------------"<< endl;

    }

    void appOptions{
        string option;
        cout << "Please enter a useable option" << endl;
        cin >> "-> " >> option

    }
}