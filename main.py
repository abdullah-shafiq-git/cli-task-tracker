import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("\n==============================")
    print("    COMMAND-LINE TASK TRACKER   ")
    print("==============================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("==============================")

def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks available!")
        return
    
    print("\n--- YOUR TASKS ---")
    for index, task in enumerate(tasks, start=1):
        status_icon = "✅" if task["status"] == "Completed" else "⏳"
        print(f"{index}. [{status_icon}] {task['title']} | Priority: {task['priority']} | Status: {task['status']}")

def add_task(tasks):
    title = input("\nEnter task title: ").strip()
    if not title:
        print("❌ Task title cannot be empty!")
        return
    
    print("Select Priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")
    p_choice = input("Enter priority choice (1-3, default Medium): ").strip()
    
    priority_map = {"1": "High", "2": "Medium", "3": "Low"}
    priority = priority_map.get(p_choice, "Medium")
    
    new_task = {
        "title": title,
        "priority": priority,
        "status": "Pending"
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✨ Task '{title}' added successfully!")

def mark_completed(tasks):
    if not tasks:
        print("\n📭 No tasks available to mark as completed!")
        return
    
    view_tasks(tasks)
    try:
        choice = int(input("\nEnter task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["status"] = "Completed"
            save_tasks(tasks)
            print(f"🎉 Task '{tasks[choice - 1]['title']}' marked as completed!")
        else:
            print("❌ Invalid task number entered.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task(tasks):
    if not tasks:
        print("\n📭 No tasks available to delete!")
        return
        
    view_tasks(tasks)
    try:
        choice = int(input("\nEnter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['title']}' deleted successfully!")
        else:
            print("❌ Invalid task number entered.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\n👋 Exiting Task Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()