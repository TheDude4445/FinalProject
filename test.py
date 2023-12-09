# Import necessary modules
import pytest
from FinalProject import TaskManager

# Define a pytest fixture to create a TaskManager instance
@pytest.fixture
def task_manager():
    return TaskManager()

# Helper function to clear the task manager by deleting all tasks
def clear_task_manager(task_manager):
    # Iterate through tasks and delete them
    while task_manager.tasks:
        task_manager.delete_task_from_file(1)

# Test case for adding a task to the TaskManager
def test_add_task(task_manager):
    # Add a task to the task manager
    task_manager.add_task("Task 1", "Description 1", "High")
    # Check if the task is added successfully
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0]["name"] == "Task 1"
    # Clear the task manager after the test
    clear_task_manager(task_manager)

# Test case for marking a task as completed in the TaskManager
def test_mark_task_completed(task_manager):
    # Add a task to the task manager
    task_manager.add_task("Task 1", "Description 1", "High")
    # Mark the task as completed
    task_manager.mark_task_completed(1)
    # Check if the task is marked as completed
    assert task_manager.tasks[0]["completed"] == True
    # Clear the task manager after the test
    clear_task_manager(task_manager)

# Test case for sorting tasks by priority in the TaskManager
def test_sort_tasks(task_manager):
    # Add tasks with different priorities to the task manager
    task_manager.add_task("Task 1", "Description 1", "Medium")
    task_manager.add_task("Task 2", "Description 2", "Low")
    task_manager.add_task("Task 3", "Description 3", "High")

    # Check the initial order of tasks
    assert task_manager.tasks[0]["name"] == "Task 1"
    assert task_manager.tasks[1]["name"] == "Task 2"
    assert task_manager.tasks[2]["name"] == "Task 3"

    # Sort tasks by priority
    task_manager.insertion_sort()

    # Check the order of tasks after sorting
    assert task_manager.tasks[0]["name"] == "Task 3"
    assert task_manager.tasks[1]["name"] == "Task 1"
    assert task_manager.tasks[2]["name"] == "Task 2"
    # Clear the task manager after the test
    clear_task_manager(task_manager)

# Test case for deleting a task from the TaskManager
def test_delete_task(task_manager):
    # Add tasks to the task manager
    task_manager.add_task("Task 1", "Description 1", "High")
    task_manager.add_task("Task 2", "Description 2", "Medium")
    task_manager.add_task("Task 3", "Description 3", "Low")

    # Check the initial number of tasks
    assert len(task_manager.tasks) == 3

    # Delete a task from the task manager
    task_manager.delete_task_from_file(2)

    # Check the number of tasks after deletion
    assert len(task_manager.tasks) == 2
    # Check the order of remaining tasks
    assert task_manager.tasks[0]["name"] == "Task 1"
    assert task_manager.tasks[1]["name"] == "Task 3"
    # Clear the task manager after the test
    clear_task_manager(task_manager)