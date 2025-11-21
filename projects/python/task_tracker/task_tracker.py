"""
Simple CLI to track what I need to do, what I have done, and what I'm currently working on.

This application accepts user actions and inputs as arguments, and stores the tasks in a JSON file. The user
should be able to:

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
"""
import json
import os
import sys


DATA_FILE_PATH = 'tasks.json'


# Create file if it does not exist
if not os.path.exists(DATA_FILE_PATH):
    with open(DATA_FILE_PATH, 'x') as f:
        f.write("{}")

# Validate input

# Read file
with open(DATA_FILE_PATH) as f:
    data = json.load(f)
    print(f.read())

