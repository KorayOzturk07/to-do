# TODOER - Command Line Task Manager

```
████████╗ ██████╗ ██████╗  ██████╗ ███████╗██████╗ 
╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗██╔════╝██╔══██╗
   ██║   ██║   ██║██║  ██║██║   ██║█████╗  ██████╔╝
   ██║   ██║   ██║██║  ██║██║   ██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██████╔╝╚██████╔╝███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
```

✅ Get Things Done! 🚀

## Overview

TODOER is a colorful and emoji-rich command-line task management application built with Python. It allows you to manage your tasks with features like priority levels, due dates, and task descriptions. The application uses a simple JSON file for storing tasks, making it lightweight and portable.

## Features

- 📋 **Task Management**: Add, update, remove, and mark tasks as complete
- 🎯 **Priority Levels**: Assign low, medium, or high priority to tasks (color-coded for easy recognition)
- 📅 **Due Dates**: Set and track due dates for your tasks
- 📝 **Task Descriptions**: Add detailed descriptions to your tasks
- 💾 **Persistent Storage**: Tasks are saved to a JSON file for persistent storage
- 🎨 **Colorful UI**: Enjoy a vibrant and easy-to-navigate interface with colorama
- 😀 **Emoji Support**: Visual indicators make task management more intuitive

## Installation

1. Clone the repository:
```bash
git clone https://github.com/KorayOzturk07/to-do
cd to-do
```

2. Install the required dependencies:
```bash
pip install colorama
```

3. Run the application:
```bash
python main.py
```

## Usage

When you run the application, you'll be presented with a menu of options:

1. **➕ Add a new task**: Create a new task with title, description, due date, and priority
2. **📜 List all tasks**: View all your tasks, with options to filter out completed tasks
3. **✅ Mark task as complete**: Mark a task as complete
4. **🗑️ Remove a task**: Delete a task from your list
5. **📝 Update a task**: Modify an existing task's details
6. **👋 Exit**: Close the application

### Example Task Creation

```
Enter task title: Complete project report
Enter task description (optional): Finalize the quarterly project report with all metrics and charts
Enter due date (YYYY-MM-DD) (optional): 2025-04-10
Enter priority (low/medium/high) (default: medium): high
```

### Task Display

Tasks are displayed with colored indicators:
- 🔴 High priority tasks (Red)
- 🟡 Medium priority tasks (Yellow)
- 🟢 Low priority tasks (Green)
- ✅ Completed tasks
- ⬜ Incomplete tasks

## File Structure

- `main.py`: Main application file
- `tasks.json`: JSON file that stores your tasks (created automatically)

## Data Structure

Each task contains the following information:
- Title: The name of the task
- Description: Optional detailed description
- Due Date: Optional deadline in YYYY-MM-DD format
- Priority: "low", "medium", or "high"
- Completion Status: Boolean indicating whether the task is completed
- Creation Timestamp: When the task was created

## Requirements

- Python 3.6+
- colorama

## License

GPL 3.0

## Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to submit a pull request or open an issue.

## Future Enhancements

- 🔍 Search functionality
- 🗂️ Task categories/tags
- 📊 Task statistics and reports
- 🔔 Due date notifications
- 📱 Mobile version

---

Made with ❤️ by Koray Öztürk
