import os
import json
from datetime import datetime
from colorama import init, Fore, Style, Back

# Initialize colorama
init(autoreset=True)

def display_banner():
    print(Fore.CYAN + """
████████╗ ██████╗ ██████╗  ██████╗ ███████╗██████╗ 
╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗██╔════╝██╔══██╗
   ██║   ██║   ██║██║  ██║██║   ██║█████╗  ██████╔╝
   ██║   ██║   ██║██║  ██║██║   ██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██████╔╝╚██████╔╝███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
    """ + Style.BRIGHT + Fore.YELLOW + "✅ Get Things Done! 🚀" + Style.RESET_ALL)

class Task:
    def __init__(self, title, description="", due_date=None, priority="medium", completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            priority=data["priority"],
            completed=data["completed"]
        )
        task.created_at = data["created_at"]
        return task


class TodoApp:
    def __init__(self, storage_file="tasks.json"):
        self.storage_file = storage_file
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    tasks_data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]
            except Exception as e:
                print(Fore.RED + f"⚠️ Error loading tasks: {e}")
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        try:
            with open(self.storage_file, "w") as f:
                tasks_data = [task.to_dict() for task in self.tasks]
                json.dump(tasks_data, f, indent=2)
        except Exception as e:
            print(Fore.RED + f"⚠️ Error saving tasks: {e}")
    
    def add_task(self, title, description="", due_date=None, priority="medium"):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            return removed
        return None
    
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
            return self.tasks[index]
        return None
    
    def update_task(self, index, title=None, description=None, due_date=None, priority=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if due_date is not None:
                task.due_date = due_date
            if priority is not None:
                task.priority = priority
            self.save_tasks()
            return task
        return None
    
    def list_tasks(self, show_completed=True):
        if show_completed:
            return self.tasks
        else:
            return [task for task in self.tasks if not task.completed]
    
    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]
    
    def get_tasks_by_due_date(self, date):
        return [task for task in self.tasks if task.due_date == date]


def get_priority_color(priority):
    if priority == "high":
        return Fore.RED
    elif priority == "medium":
        return Fore.YELLOW
    else:
        return Fore.GREEN


def main():
    # Display the TODOER banner
    display_banner()
    
    app = TodoApp()
    
    while True:
        print("\n" + Back.BLUE + Fore.WHITE + Style.BRIGHT + "===== 📋 MENU 📋 =====" + Style.RESET_ALL)
        print(Fore.MAGENTA + "1. ➕ Add a new task")
        print(Fore.CYAN + "2. 📜 List all tasks")
        print(Fore.GREEN + "3. ✅ Mark task as complete")
        print(Fore.YELLOW + "4. 🗑️  Remove a task")
        print(Fore.BLUE + "5. 📝 Update a task")
        print(Fore.RED + "6. 👋 Exit")
        
        choice = input(Fore.WHITE + "Enter your choice (1-6): ")
        
        if choice == "1":
            print(Fore.MAGENTA + "\n➕ Adding a new task:")
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            due_date = input("Enter due date (YYYY-MM-DD) (optional): ")
            due_date = due_date if due_date else None
            priority = input("Enter priority (low/medium/high) (default: medium): ")
            priority = priority if priority in ["low", "medium", "high"] else "medium"
            
            app.add_task(title, description, due_date, priority)
            print(Fore.GREEN + "✅ Task added successfully! 🎉")
            
        elif choice == "2":
            show_completed = input("Show completed tasks? (y/n): ").lower() == "y"
            tasks = app.list_tasks(show_completed)
            
            if not tasks:
                print(Fore.YELLOW + "📭 No tasks found.")
            else:
                print(Fore.CYAN + "\n📜 Your Tasks:")
                for i, task in enumerate(tasks):
                    priority_color = get_priority_color(task.priority)
                    status = Fore.GREEN + "✅" if task.completed else Fore.RED + "⬜"
                    priority_symbol = {
                        "high": "🔴",
                        "medium": "🟡",
                        "low": "🟢"
                    }.get(task.priority, "")
                    
                    due = f"(📅: {task.due_date})" if task.due_date else ""
                    print(f"{i+1}. {status} {Fore.WHITE + task.title} - {priority_color + priority_symbol + task.priority} {Fore.BLUE + due}")
                    if task.description:
                        print(f"   {Fore.CYAN}Description: {Fore.WHITE}{task.description}")
                    
        elif choice == "3":
            try:
                index = int(input(Fore.GREEN + "Enter task number to mark as complete: ")) - 1
                task = app.complete_task(index)
                if task:
                    print(Fore.GREEN + f"✅ Task '{task.title}' marked as complete! 🎉")
                else:
                    print(Fore.RED + "⚠️ Invalid task number.")
            except ValueError:
                print(Fore.RED + "⚠️ Please enter a valid number.")
                
        elif choice == "4":
            try:
                index = int(input(Fore.YELLOW + "Enter task number to remove: ")) - 1
                task = app.remove_task(index)
                if task:
                    print(Fore.YELLOW + f"🗑️ Task '{task.title}' removed!")
                else:
                    print(Fore.RED + "⚠️ Invalid task number.")
            except ValueError:
                print(Fore.RED + "⚠️ Please enter a valid number.")
                
        elif choice == "5":
            try:
                index = int(input(Fore.BLUE + "Enter task number to update: ")) - 1
                if 0 <= index < len(app.tasks):
                    task = app.tasks[index]
                    print(Fore.BLUE + f"📝 Updating task: {task.title}")
                    
                    title = input(f"Enter new title (current: {task.title}) (leave empty to keep current): ")
                    description = input(f"Enter new description (current: {task.description}) (leave empty to keep current): ")
                    due_date = input(f"Enter new due date (current: {task.due_date}) (leave empty to keep current): ")
                    priority = input(f"Enter new priority (current: {task.priority}) (leave empty to keep current): ")
                    
                    app.update_task(
                        index,
                        title=title if title else None,
                        description=description if description else None,
                        due_date=due_date if due_date else None,
                        priority=priority if priority in ["low", "medium", "high"] else None
                    )
                    print(Fore.GREEN + "✅ Task updated successfully! 🎉")
                else:
                    print(Fore.RED + "⚠️ Invalid task number.")
            except ValueError:
                print(Fore.RED + "⚠️ Please enter a valid number.")
                
        elif choice == "6":
            print(Fore.CYAN + "👋 Goodbye! Have a productive day! 🌟")
            break
            
        else:
            print(Fore.RED + "⚠️ Invalid choice, please try again.")


if __name__ == "__main__":
    main()