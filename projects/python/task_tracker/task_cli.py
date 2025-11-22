"""
Simple CLI to track what I need to do, what I have done, and what I'm currently working on.

This application accepts user actions and inputs as arguments, and stores the tasks in a
JSON file. The user should be able to:

- Add, update, and delete tasks
- Mark a task as in progress or done
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

Each task should have the following properties:
- id: A unique identifier for the task
- description: A short description of the task
- status: The status of the task (to-do, in-progress, done)
- createdAt: The date and time when the task was created
- updatedAt: The date and time when the task was last updated

Constraints:
- Use positional arguments in CLI to accept user inputs
- Use a JSON file to store the tasks in the current directory
- The JSON file should be created if it does not exist
- Use the native file system module to interact with the JSON file
- Do not use external libraries or frameworks to build this project
- Ensure to handle errors and edge cases gracefully

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


DATA_FILE_PATH = 'data.json'


def get_data_from_file() -> dict:
    # Create data file if it does not exist
    if not os.path.exists(DATA_FILE_PATH):
        write_data_to_file(dict())
    with open(DATA_FILE_PATH) as f:
        data_dict = json.load(f)
        return data_dict

def write_data_to_file(data: dict):
    with open(DATA_FILE_PATH, 'w') as f:
        # print(data)
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
    print(data)


def add_task(description="None", status="to-do") -> dict:
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
    return data


def delete_task(remove_task_id: str):
    data_dict = get_data_from_file()
    if remove_task_id not in data_dict:
        print(f"Error: Task with ID {remove_task_id} not in data file")
        return
    data_dict.pop(remove_task_id)
    new_data_dict = dict()
    for task_id, task_map in data_dict.items():
        task_id = int(task_id)
        if task_id > int(remove_task_id):
            task_id -= 1
        new_data_dict[task_id] = task_map
    write_data_to_file(new_data_dict)
    return new_data_dict



def main():
    # data = get_data_from_json_file()
    add_task("laundry")
    add_task("groceries", "in-progress")
    add_task("homework")
    add_task("work")
    add_task("study")
    list_all_tasks()
    list_all_tasks()
    delete_task("3")
    os.remove("data.json")

if __name__ == "__main__":
    main()
