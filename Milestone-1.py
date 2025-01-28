# Welcome message
print("Welcome to the Task Management Program!")
print("This program will help you practice Python basics.")

# Main menu function using a loop
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")
        
        # Get user input
        choice = input("Enter your choice (1/2/3): ")
        
        # Process user choice
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Thank you for using the Task Management Program!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Initialize an empty list for tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to view tasks
def view_tasks():
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks added yet!")

# Run the program
main_menu()
