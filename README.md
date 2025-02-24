# Task Management Program

This is a simple command-line task management program written in Python. It allows users to add, view, and remove tasks, which are stored in a text file for persistence.

## Features

- **Add Task**: Add a new task to the list. The program ensures no duplicate tasks are added.
- **View Tasks**: Display all tasks with their corresponding numbers.
- **Remove Task**: Remove a task by selecting its number from the list.
- **Persistence**: Tasks are saved to a file (`tasks.txt`) and loaded upon program startup.

## How to Use

1. **Run the Program**: Execute the Python script to start the program.
2. **Menu Options**:
   - **1. Add Task**: Enter a new task to add to the list.
   - **2. View Tasks**: View all tasks currently in the list.
   - **3. Remove Task**: Remove a task by entering its corresponding number.
   - **4. Exit**: Exit the program.

## Code Structure

- **`TASKS_FILE`**: The file where tasks are stored (`tasks.txt`).
- **`load_tasks()`**: Loads tasks from the file into a list.
- **`save_tasks()`**: Saves the current list of tasks to the file.
- **`display_menu()`**: Displays the main menu options.
- **`add_task()`**: Adds a new task to the list after checking for duplicates.
- **`view_tasks()`**: Displays all tasks with their numbers.
- **`remove_task()`**: Removes a task based on its number.
- **`main()`**: The main function that runs the program and handles user input.

## Example Usage

```bash
$ python Milestone-2.py

Task Management Program
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: 1
Enter a new task: Buy groceries
Task 'Buy groceries' added successfully.

Task Management Program
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: 2

Your Tasks:
1. Buy groceries

Task Management Program
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: 3

Your Tasks:
1. Buy groceries
Enter the task number to remove: 1
Task 'Buy groceries' removed successfully.

Task Management Program
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice: 4
Exiting program. 
