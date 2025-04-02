# todo.py
from utils import validate_input

tasks = []

def add_task(task, priority=None):
    if priority is not None:
        tasks.append((task, priority))
    else:
        tasks.append(task)
    print(f"Added: {task}")

def list_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            if isinstance(task, tuple):
                 print(f"{i+1}. {task[0]} (Priority: {task[1]})")
            else:
                print(f"{i+1}. {task}")

def delete_task(index):
    try:
        del tasks[index - 1]
        print("Task deleted.")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        command = input("Enter command (add/list/delete/quit): ")
        if command == "add":
            task = validate_input("Enter task: ", lambda x: len(x) > 0)
            priority = validate_input("Enter priority (optional, number): ", lambda x: x.isdigit() or x == "")
            if priority:
                add_task(task, int(priority))
            else:
                add_task(task)
        elif command == "list":
            list_tasks()
        elif command == "delete":
            try:
                index = int(validate_input("Enter task number to delete: ", lambda x: x.isdigit()))
                delete_task(index)
            except ValueError:
                print("Invalid input.  Enter a number.")
        elif command == "quit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
