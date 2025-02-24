import os

# File where tasks will be stored
TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display the menu
def display_menu():
    print("\nTask Management Program")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
# Add a new task with validation (no duplicates)
def add_task():
    task = input("Enter a new task: ").strip()
    if task in tasks:
        print("This task already exists.")
    else:
        tasks.append(task)
        save_tasks()
        print(f"Task '{task}' added successfully.")

# View all tasks with numbering
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Remove a task by selecting its number
def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_num < len(tasks):
                removed_task = tasks.pop(task_num)
                save_tasks()
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Load tasks on startup
tasks = load_tasks()

# Run the program
main()
