import os
import random

# File where tasks will be stored
TASKS_FILE = "tasks.txt"

class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    # Load tasks from file
    def load_tasks(self):
        if not os.path.exists(TASKS_FILE):
            return []
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]

    # Save tasks to file
    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    # Add a new task with validation (no duplicates)
    def add_task(self):
        task = input("Enter a new task: ").strip()
        if task in self.tasks:
            print("This task already exists.")
        else:
            self.tasks.append(task)
            self.save_tasks()
            print(f"Task '{task}' added successfully.")

    # View all tasks with numbering
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    # Remove a task by selecting its number
    def remove_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                task_num = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_num < len(self.tasks):
                    removed_task = self.tasks.pop(task_num)
                    self.save_tasks()
                    print(f"Task '{removed_task}' removed successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # Suggest a random task
    def suggest_random_task(self):
        if not self.tasks:
            print("No tasks available to suggest.")
        else:
            print(f"Suggested Task: {random.choice(self.tasks)}")

    # Sort tasks alphabetically
    def sort_tasks(self):
        if not self.tasks:
            print("No tasks available to sort.")
        else:
            self.tasks.sort()
            self.save_tasks()
            print("Tasks sorted alphabetically.")

# Main function to run the program
def main():
    manager = TaskManager()
    while True:
        print("\nTask Management Program")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Get a Random Task Suggestion")
        print("5. Sort Tasks Alphabetically")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.remove_task()
        elif choice == "4":
            manager.suggest_random_task()
        elif choice == "5":
            manager.sort_tasks()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

# Run the program
if __name__ == "__main__":
    main()
