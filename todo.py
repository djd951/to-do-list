import os
import pickle

class Task:
    def __init__(self, title, description="", completed=False):
        self.title = title
        self.description = description
        self.completed = completed

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        self.tasks.append(Task(title, description))
        print("Task added successfully!")

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "[x]" if task.completed else "[ ]"
            print(f"{i}. {status} {task.title} - {task.description}")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    def save_tasks(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.tasks, f)
            print("Tasks saved successfully!")

    def load_tasks(self, filename):
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'rb') as f:
                self.tasks = pickle.load(f)
                print("Tasks loaded successfully!")
        else:
            print("No previous tasks found.")

def main():
    todo_list = TodoList()
    filename = "tasks.pkl"

    if os.path.exists(filename):
        todo_list.load_tasks(filename)

    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Mark Task as Completed\n4. Delete Task\n5. Save and Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            todo_list.add_task(title, description)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            todo_list.save_tasks(filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
