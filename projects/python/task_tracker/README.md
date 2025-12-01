# Description

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

# Usage

```
$ python3 task_cli.py --help 
Usage: 
 task_cli <command> 


Available Commands: 
 add "<description>"            Add a new task
 delete <id>                    Delete task 
 list [done|todo|in-progress]   List tasks 
 mark-in-progress <id>          Change status to in-progress
 mark-done <id>                 Change status to done
 update <id> "description"      Update task description
```
