import sys

# To-do list dictionary to store tasks with a status
todo_list = {}

def display_menu():
    print("\nTo-Do List Application")
    print("=======================")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Delete a task")
    print("4. View all tasks")
    print("5. Exit")

def add_task():
    task_name = input("Enter the task name: ")
    status = input("Enter the task status (Pending/Completed): ")
    todo_list[task_name] = status
    print(f"Task '{task_name}' added.")

def update_task():
    task_name = input("Enter the task name to update: ")
    if task_name in todo_list:
        status = input("Enter the new status (Pending/Completed): ")
        todo_list[task_name] = status
        print(f"Task '{task_name}' updated.")
    else:
        print(f"Task '{task_name}' not found.")

def delete_task():
    task_name = input("Enter the task name to delete: ")
    if task_name in todo_list:
        del todo_list[task_name]
        print(f"Task '{task_name}' deleted.")
    else:
        print(f"Task '{task_name}' not found.")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for task, status in todo_list.items():
            print(f"- {task}: {status}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            update_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


main()