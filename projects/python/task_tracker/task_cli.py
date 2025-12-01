#!/usr/bin/env python
"""
Simple CLI to track what I need to do, what I have done, and what I'm currently working on.
Please see README file for details about usage
"""

from datetime import datetime
import json
import os
import sys

DATA_FILE_PATH = 'data.json'


def get_data_from_file(file_path=DATA_FILE_PATH) -> dict:
    """Read data from json file, create empty json if file does not exist"""
    if not os.path.exists(file_path):
        write_data_to_file({})
    with open(file_path, "r", encoding="utf-8") as f:
        data_dict = json.load(f)
        return data_dict

def write_data_to_file(data: dict, data_file_path=DATA_FILE_PATH):
    """Opens JSON file and writes dictionary, replacing contents"""
    with open(data_file_path, 'w', encoding="utf-8") as f:
        f.write(json.dumps(data))

def get_tasks_by_status(status: str) -> dict:
    """Get all tasks that have the provided status"""
    data = get_data_from_file()
    tasks_by_status_dict = dict()
    for task_id, task_map in data.items():
        if task_map["status"] == status:
            tasks_by_status_dict[task_id] = task_map
    return tasks_by_status_dict


def list_all_tasks():
    """Gets and prints all tasks of data file"""
    data = get_data_from_file()
    if not data:
        print("Tasks list is empty")
        return data
    print_tasks(data)
    return data


def add_task(description="None", status="todo") -> dict:
    """Adds task into data file"""
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
    """Removes tasks from tasks lis by ID"""
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

def update_task_description(task_id: str, description: str) -> dict:
    """Update description of task"""
    data_dict = get_data_from_file()
    if task_id not in data_dict:
        print(f"Error, {task_id} is not in the tasks list")
        return data_dict
    data_dict[task_id]['description'] = description
    print(f"Successfully updated task_id {task_id} with description: {description}")
    write_data_to_file(data_dict)
    return data_dict

def update_task_status(task_id: str, status: str) -> dict:
    """Update task status"""
    data_dict = get_data_from_file()
    if task_id not in data_dict:
        print(f"Error, {task_id} is not in the tasks list")
        return data_dict
    data_dict[task_id]['status'] = status
    write_data_to_file(data_dict)
    return data_dict

def execute_task_cli(args: list) -> dict | None:
    """Parses commandline arguments and executes commands"""
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
                tasks_by_status =  get_tasks_by_status(status)
                if not tasks_by_status:
                    print(f"List has no tasks with status: {status}")
                print_tasks(tasks_by_status)
                return tasks_by_status
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
    """Prints usage"""
    help_string = ("Usage: \n task_cli <command> \n\nAvailable Commands: \n "
                   "add \"<description>\" \t\tAdd a new task\n "
                   "delete <id> \t\t\tDelete task \n "
                   "list [done|todo|in-progress] \tList tasks \n "
                   "mark-in-progress <id>\t\tChange status to in-progress\n "
                   "mark-done <id>\t\t\tChange status to done\n "
                   "update <id> \"description\" \tUpdate task description\n"
                   )
    print(help_string)

def print_tasks(data_dict) -> bool:
    """Formatted print of tasks"""
    if not data_dict:
        return False
    for task_id, task_map in data_dict.items():
        print(f"Task ID: {task_id}")
        for task, value in task_map.items():
            print(task + ": " + value)
        print("")
    return True


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_help()
    else:
        execute_task_cli(sys.argv[1:])
