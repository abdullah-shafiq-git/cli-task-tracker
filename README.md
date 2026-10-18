# Command-Line Task Tracker

A simple, lightweight, and interactive Command-Line Interface (CLI) application built in Python to manage daily tasks, track priorities, and retain task data across sessions using a local JSON file.

---

## 🚀 Features

- **Add Tasks**: Easily insert new daily tasks with customizable priority levels (**High**, **Medium**, **Low**).
- **View Tasks**: Display all saved tasks along with their current status (**Pending / Completed**) and priority.
- **Track Status**: Mark tasks as completed with interactive menu options.
- **Delete Tasks**: Remove unwanted or finished tasks from your list.
- **Data Persistence**: Automatically creates and updates a `tasks.json` file to store your tasks permanently between sessions.

---

## 🛠️ Project Structure

```text
cli-task-tracker/
│
├── main.py          # Core logic & CLI application
├── tasks.json       # Auto-created storage file for tasks
└── README.md        # Project documentation