import json
from colorama import Fore, Style, init


class Task:
    def __init__(self, description, due_date=None, category=None):
        # Task initialization logic


class ToDoList:
    def __init__(self, filename="todolist.json"):
        self.tasks = []
        self.filename = filename
        self.load_from_file()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_to_file()

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def mark_as_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] += " [Completed]"
            self.save_to_file()

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            self.save_to_file()

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            # File does not exist (first run), ignore the error
            pass
        except json.JSONDecodeError:
            # Invalid JSON format, handle the error as needed
            print("Error: Invalid JSON format in the file.")


# User interface logic
def main():
    todo_list = ToDoList()

    while True:
        # Display menu options and get user input
        # Perform actions based on user input

if __name__ == "__main__":
    main()
