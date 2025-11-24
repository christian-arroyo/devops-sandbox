#!/usr/bin/env python
"""
Simple CLI to track what I need to do, what I have done, and what I'm currently working on.

This application accepts user actions and inputs as arguments, and stores the tasks in a
JSON file. The user should be able to:

- Add, update, and delete tasks
- Mark a task as in-progress or done
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

Each task has the following properties:
- id: A unique identifier for the task
- description: A short description of the task
- status: The status of the task (to-do, in-progress, done)
- createdAt: The date and time when the task was created
- updatedAt: The date and time when the task was last updated

# Adding a new task
task-cli add "Buy groceries"

# Output: Task added successfully (ID: 1)
# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list to-do
task-cli list in-progress
"""
from datetime import datetime
import json
import os
import sys

DATA_FILE_PATH = 'data.json'


def get_data_from_file(file_path=DATA_FILE_PATH) -> dict:
    """Read data from json file"""
    # Create data file if it does not exist
    if not os.path.exists(file_path):
        write_data_to_file(dict())
    with open(file_path) as f:
        data_dict = json.load(f)
        return data_dict

def write_data_to_file(data: dict, data_file_path=DATA_FILE_PATH):
    with open(data_file_path, 'w') as f:
        f.write(json.dumps(data))

def get_tasks_by_status(status):
    data = get_data_from_file()
    tasks_by_status_dict = dict()
    for task_id, task_map in data.items():
        if task_map["status"] == status:
            tasks_by_status_dict[task_id] = task_map
    return tasks_by_status_dict


def list_all_tasks():
    data = get_data_from_file()
    __print_tasks(data)
    return data


def add_task(description="None", status="todo") -> dict:
    datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = get_data_from_file()
    task_id = len(data)
    data[task_id] = {
        "description": description,
        "status": status,
        "createdAt": datetime_now,
        "updatedAt": datetime_now
    }
    write_data_to_file(data)
    print(f"Successfully created task with ID {task_id}")
    return data


def delete_task(remove_task_id: str):
    data_dict = get_data_from_file()
    if remove_task_id not in data_dict:
        print(f"Error: Task with ID {remove_task_id} is not in the tasks list")
        return
    data_dict.pop(remove_task_id)
    print(f"Successfully removed task with task ID {remove_task_id}")
    new_data_dict = dict()
    # Recalculate each task_id
    for task_id, task_map in data_dict.items():
        task_id = int(task_id)
        if task_id > int(remove_task_id):
            task_id -= 1
        new_data_dict[task_id] = task_map
    write_data_to_file(new_data_dict)
    return new_data_dict

def update_task_description(task_id, description) -> dict:
    data_dict = get_data_from_file()
    print("HEELLLOOO")
    if task_id not in data_dict:
        print(f"Error, {task_id} is not in the tasks list")
        return data_dict
    data_dict[task_id]['description'] = description
    print(f"Successfully updated task_id {task_id} with description: {description}")
    write_data_to_file(data_dict)
    return data_dict

def update_task_status(task_id: str, status: str) -> dict:
    data_dict = get_data_from_file()
    if task_id not in data_dict:
        print(f"Error, {task_id} is not in the tasks list")
        return data_dict
    data_dict[task_id]['status'] = status
    write_data_to_file(data_dict)
    return data_dict

def execute_task_cli(args: list):
    """Parses commandline arguments"""
    if not args:
        print_help()
    command = args[0]
    if len(args) == 1 and command == "list":
        return list_all_tasks()
    elif len(args) == 2:
        if command == "add":
            return add_task(args[1])
        elif command == "delete":
            if is_str_an_int(args[1]):
                return delete_task(args[1])
        elif command == "mark-in-progress":
            if is_str_an_int(args[1]):
                return update_task_status(args[1], "in-progress")
        elif command == "mark-done":
            if is_str_an_int(args[1]):
                return update_task_status(args[1], "done")
        elif command == "list":
            status = args[1]
            if status in ["done", "todo", "in-progress"]:
                return get_tasks_by_status(status)
    elif len(args) == 3:
        if command == "update":
            if is_str_an_int(args[1]):
                return update_task_description(args[1], args[2])
    print_help()


def is_str_an_int(s) -> bool:
    """Checks if a string can be converted to an int. This is used to validate task_id strings"""
    try:
        int(s)
    except TypeError:
        return False
    except ValueError:
        return False
    return True

def print_help():
    help_string = ("Usage: \n task-cli <command> \n\nAvailable Commands: \n "
                   "add \"<description>\" \t\tAdd a new task\n "
                   "delete <id> \t\t\tDelete task \n "
                   "list [done|todo|in-progress] \tList tasks \n "
                   "mark-in-progress <id>\t\tChange status to in-progress\n "
                   "mark-done <id>\t\t\tChange status to done\n "
                   "update <id> \"description\" \tUpdate task description\n"
                   )
    print(help_string)

def __print_tasks(data_dict) -> bool:
    if not data_dict:
        print("The tasks list is empty")
        return False
    for task_id, task_map in data_dict.items():
        print(f"Task ID: {task_id}")
        for task, value in task_map.items():
            print(task + ": " + value)
        print("")
    return True

def main():
    execute_task_cli(sys.argv[1:])


if __name__ == "__main__":
    main()
