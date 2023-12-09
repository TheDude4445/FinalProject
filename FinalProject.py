import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pytest

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.priorities = {"High": [], "Medium": [], "Low": []}
        self.load_tasks_from_file()  # Load tasks from the file during initialization

    def add_task(self, name, description, priority):
        priority = priority.capitalize()
        task = {"name": name, "description": description, "priority": priority, "completed": False}
        self.tasks.append(task)
        self.priorities[priority].append(task)
        self.save_tasks_to_file()  # Save tasks to the file after adding

    def view_tasks(self):
        self.load_tasks_from_file()  # Reload tasks from the file before displaying
        if not self.tasks:
            return "No tasks in the list."
        
        result = "Task List:\n"
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            result += f"{index}. {task['name']} - {task['description']} (Priority: {task['priority']}) - {status}\n"
        return result

    def mark_task_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            self.save_tasks_to_file()  # Save tasks to the file after marking as completed
            return "Task marked as completed."
        else:
            return "Invalid task index."

    def sort_tasks_by_priority(self):
        self.tasks = sorted(self.tasks, key=lambda x: ("High", "Medium", "Low").index(x["priority"]))
        self.save_tasks_to_file()  # Save tasks to the file after sorting

    def insertion_sort(self):
        for i in range(1, len(self.tasks)):
            current_task = self.tasks[i]
            j = i - 1
            while j >= 0 and self.priority_value(current_task["priority"]) > self.priority_value(self.tasks[j]["priority"]):
                self.tasks[j + 1] = self.tasks[j]
                j -= 1
            self.tasks[j + 1] = current_task
        self.save_tasks_to_file()  # Save tasks to the file after insertion sort

    def priority_value(self, priority):
        priority_values = {"High": 3, "Medium": 2, "Low": 1}
        return priority_values[priority]

    def save_tasks_to_file(self, filename="task_list.txt"):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task['name']}|{task['description']}|{task['priority']}|{task['completed']}\n")

    def load_tasks_from_file(self, filename="task_list.txt"):
        self.tasks = []
        self.priorities = {"High": [], "Medium": [], "Low": []}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    values = line.strip().split('|')
                    name, description, priority, completed = values
                    task = {"name": name, "description": description, "priority": priority, "completed": completed == 'True'}
                    self.tasks.append(task)
                    self.priorities[priority].append(task)
        except FileNotFoundError:
            pass

    def delete_task_from_file(self, task_index, filename="task_list.txt"):
        if 0 < task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            self.priorities[deleted_task['priority']].remove(deleted_task)
            self.save_tasks_to_file(filename)
            return "Task deleted successfully."
        else:
            return "Invalid task index."


class TaskManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")
        self.task_manager = TaskManager()
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Helvetica', 12))
        style.configure("TLabel", font=('Helvetica', 12))

        self.label = ttk.Label(self.master, text="Task Manager Menu:", style="TLabel")
        self.label.pack(pady=10)

        self.add_button = ttk.Button(self.master, text="Add Task", command=self.add_task, style="TButton")
        self.add_button.pack(pady=10)

        self.view_button = ttk.Button(self.master, text="View Tasks", command=self.view_tasks, style="TButton")
        self.view_button.pack(pady=10)

        self.mark_completed_button = ttk.Button(self.master, text="Mark Task as Completed", command=self.mark_task_completed, style="TButton")
        self.mark_completed_button.pack(pady=10)

        self.sort_button = ttk.Button(self.master, text="Sort Tasks by Priority", command=self.sort_tasks, style="TButton")
        self.sort_button.pack(pady=10)

        self.delete_button = ttk.Button(self.master, text="Delete Task", command=self.delete_task, style="TButton")
        self.delete_button.pack(pady=10)

        self.exit_button = ttk.Button(self.master, text="Exit", command=self.master.destroy, style="TButton")
        self.exit_button.pack(pady=10)

    def add_task(self):
        name = self.get_input("Task Name:")
        description = self.get_input("Task Description:")
        priority = self.get_input("Task Priority (High, Medium, Low):").capitalize()

        if priority not in ["High", "Medium", "Low"]:
            priority = None
            messagebox.showerror("Error", "Priority must be High, Medium, or Low")
                
        if name and description and priority:
            self.task_manager.add_task(name, description, priority)
            messagebox.showinfo("Success", "Task added successfully.")
        else:
            messagebox.showerror("Error", "Invalid input. Please fill in all fields.")

    def view_tasks(self):
        result = self.task_manager.view_tasks()
        messagebox.showinfo("Task List", result)

    def mark_task_completed(self):
        result = self.task_manager.view_tasks()
        task_index = self.get_input("Enter the index of the task to mark as completed:")
        
        if task_index.isdigit():
            task_index = int(task_index)
            result = self.task_manager.mark_task_completed(task_index)
            messagebox.showinfo("Success", result)
        else:
            messagebox.showerror("Error", "Invalid input. Please enter a valid index.")

    def sort_tasks(self):
        self.task_manager.insertion_sort()
        messagebox.showinfo("Success", "Tasks sorted by priority.")

    def delete_task(self):
        result = self.task_manager.view_tasks()
        task_index = self.get_input("Enter the index of the task to delete:")
        
        if task_index.isdigit():
            task_index = int(task_index)
            result = self.task_manager.delete_task_from_file(task_index)
            messagebox.showinfo("Success", result)
        else:
            messagebox.showerror("Error", "Invalid input. Please enter a valid index.")

    def get_input(self, prompt):
        return simpledialog.askstring("Input", prompt)
    
    # Run the GUI
root = tk.Tk()
app = TaskManagerGUI(root)
root.mainloop()