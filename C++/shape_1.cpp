#include <iostream>
#include <vector>
#include <string>

using namespace std;

class UserGreeting {
public:
    UserGreeting() {
        cout << "\nWelcome to the RADAR Application!\n" << endl;
        cout << "---------------RADAR-----------------" << endl;
        cout << "R: Reminder--------------------------" << endl;
        cout << "A: And-------------------------------" << endl;
        cout << "D: Deadline--------------------------" << endl;
        cout << "A: Assistance------------------------" << endl;
        cout << "R: Remote----------------------------" << endl;
        cout << "-------------------------------------" << endl;
    }
};

class TaskClass {
private:
    static int nextTaskID; // Static variable to keep 
    int taskID;
    string taskName;

public:
    // A method used to add a task to the to-do list
    Task(const string& name) : taskName(name) ,taskID(nextTaskID++) {}

    void display() const{
        cout << "Task ID: " << taskID << "Task Name:" << taskName << endl;
    }

    void  taskName() {
        // Prints the task name
    }

    void timeNeeded() {
        //prints out the time needed for the task to be done given by the user
    }

    void Description(){
        //Also provided by the user gives the user an optional options to give a descriotion of the task
    }
    
    void status() {
        // telss the user if the task is completed or not 
    }

    void  dueDate(){
        //given by the user the due date of the task
    }

    void priorityLevel(){
        //telss the user the priority level of the task also given by the user
    } // must use contructor getter and setter methods for the properties 

class ToDoList {
private:
    vector<string> tasks;

public:
    void addTask(const string& task) {
        tasks.push_back(task);
    }

    void removeTask(const string& task) {
        auto it = find(tasks.begin(), tasks.end(), task);
        if (it != tasks.end()) {
            tasks.erase(it);
        }
    }

    void modifyTask(const string& oldTask, const string& newTask) {
        auto it = find(tasks.begin(), tasks.end(), oldTask);
        if (it != tasks.end()) {
            *it = newTask;
        }
    }

    void displayTasks() const {
        cout << "To-Do List:" << endl;
        for (const auto& task : tasks) {
            cout << "- " << task << endl;
        }
    }

    void saveToFile(const string& filename) const {
        ofstream file(filename);
        if (file.is_open()) {
            for (const auto& task : tasks) {
                file << task << endl;
            }
            cout << "Tasks saved to file: " << filename << endl;
        } else {
            cerr << "Unable to open file: " << filename << endl;
        }
    }

    void loadFromFile(const string& filename) {
        ifstream file(filename);
        if (file.is_open()) {
            string task;
            tasks.clear();  // Clear existing tasks before loading
            while (getline(file, task)) {
                tasks.push_back(task);
            }
            cout << "Tasks loaded from file: " << filename << endl;
        } else {
            cerr << "Unable to open file: " << filename << endl;
        }
    }

    void notifyUser() const {
        cout << "Reminder: You have tasks to complete!" << endl;
    } // update to affect the gui of my OS which is a gnome desktop for Pop_OS! as in a real notification appearing at the top
};


};
