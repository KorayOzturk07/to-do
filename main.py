def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    status, task = line.strip().split(",", 1)
                    tasks.append({"task": task, "completed": bool(int(status))})
                except ValueError:
                    print(f"Warning: Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        pass  # File doesn’t exist yet, return empty list
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            status = "1" if task["completed"] else "0"
            file.write(f"{status},{task['task']}\n")

def add_task(tasks, task):
    if task.strip():  # Ensure task isn’t empty
        tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks available!")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

def complete_task(tasks, index):
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print(f"Task {index} completed")
    else:
        print("Invalid task number!")

def delete_task(tasks, index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Task deleted: {removed['task']}")
    else:
        print("Invalid task number!")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Your choice (1-5): ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            task = input("New task: ")
            add_task(tasks, task)
        elif choice == "3":
            list_tasks(tasks)
            try:
                index = int(input("Enter the task number to complete: "))
                complete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            list_tasks(tasks)
            try:
                index = int(input("Enter the task number to delete: "))
                delete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()