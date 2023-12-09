import pytest
from FinalProject import TaskManager

@pytest.fixture
def task_manager():
    return TaskManager()

def clear_task_manager(task_manager):
    # Iterate through tasks and delete them
    while task_manager.tasks:
        task_manager.delete_task_from_file(1)

def test_add_task(task_manager):
    task_manager.add_task("Task 1", "Description 1", "High")
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0]["name"] == "Task 1"
    clear_task_manager(task_manager)

def test_mark_task_completed(task_manager):
    task_manager.add_task("Task 1", "Description 1", "High")
    task_manager.mark_task_completed(1)
    assert task_manager.tasks[0]["completed"] == True
    clear_task_manager(task_manager)

def test_sort_tasks(task_manager):
    task_manager.add_task("Task 1", "Description 1", "Medium")
    task_manager.add_task("Task 2", "Description 2", "Low")
    task_manager.add_task("Task 3", "Description 3", "High")

    assert task_manager.tasks[0]["name"] == "Task 1"
    assert task_manager.tasks[1]["name"] == "Task 2"
    assert task_manager.tasks[2]["name"] == "Task 3"

    task_manager.sort_tasks_by_priority()

    assert task_manager.tasks[0]["name"] == "Task 3"
    assert task_manager.tasks[1]["name"] == "Task 1"
    assert task_manager.tasks[2]["name"] == "Task 2"
    clear_task_manager(task_manager)

def test_delete_task(task_manager):
    task_manager.add_task("Task 1", "Description 1", "High")
    task_manager.add_task("Task 2", "Description 2", "Medium")
    task_manager.add_task("Task 3", "Description 3", "Low")

    assert len(task_manager.tasks) == 3

    task_manager.delete_task_from_file(2)

    assert len(task_manager.tasks) == 2
    assert task_manager.tasks[0]["name"] == "Task 1"
    assert task_manager.tasks[1]["name"] == "Task 3"
    clear_task_manager(task_manager)