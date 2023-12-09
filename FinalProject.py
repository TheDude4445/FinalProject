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

    def add_task(self, name, description, priority):
        priority = priority.capitalize()
        task = {"name": name, "description": description, "priority": priority, "completed": False}
        self.tasks.append(task)
        self.priorities[priority].append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        print("Task List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['name']} - {task['description']} (Priority: {task['priority']}) - {status}")

    def mark_task_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def sort_tasks_by_priority(self):
        self.tasks = sorted(self.tasks, key=lambda x: ("High", "Medium", "Low").index(x["priority"]))

    def insertion_sort(self):
        for i in range(1, len(self.tasks)):
            current_task = self.tasks[i]
            j = i - 1
            while j >= 0 and self.priority_value(current_task["priority"]) > self.priority_value(self.tasks[j]["priority"]):
                self.tasks[j + 1] = self.tasks[j]
                j -= 1
            self.tasks[j + 1] = current_task
    def priority_value(self, priority):
        priority_values = {"High": 3, "Medium": 2, "Low": 1}
        return priority_values[priority]

# Create an instance of TaskManager
task_manager = TaskManager()

while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Sort Tasks by Priority")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Task Name: ")
        description = input("Task Description: ")
        priority = input("Task Priority (High, Medium, Low): ")
        task_manager.add_task(name, description, priority)
        print("Task added successfully.")
    elif choice == "2":
        task_manager.view_tasks()
    elif choice == "3":
        task_manager.view_tasks()
        task_index = int(input("Enter the index of the task to mark as completed: "))
        task_manager.mark_task_completed(task_index)
    elif choice == "4":
        task_manager.insertion_sort()
        print("Tasks sorted by priority.")
    elif choice == "5":
        print("Exiting Task Manager.")
        break
    else:
        print("Invalid choice. Please select a valid option.")