import json
import os

# File to store tasks
TASK_FILE = 'tasks.json'

# Load existing tasks from the file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks, description):
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {
        'description': description,
        'completed': False
    }
    save_tasks(tasks)
    print(f"Task '{description}' added.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task_id, task in tasks.items():
            status = "Completed" if task['completed'] else "Pending"
            print(f"{task_id}. {task['description']} [{status}]")

# Delete a task
def delete_task(tasks, task_id):
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        print(f"Task {task_id} deleted.")
    else:
        print(f"Task {task_id} not found.")

# Mark a task as complete
def complete_task(tasks, task_id):
    if task_id in tasks:
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
        print(f"Task {task_id} marked as complete.")
    else:
        print(f"Task {task_id} not found.")

# Main function to interact with the user
def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_id = input("Enter task ID to delete: ")
            delete_task(tasks, task_id)
        elif choice == '4':
            task_id = input("Enter task ID to mark as complete: ")
            complete_task(tasks, task_id)
        elif choice == '5':
            print("Exiting the To-Do List Manager.")
            break
        else:
            print("Invalid option, please try again.")

# Directly call main()
# main()
