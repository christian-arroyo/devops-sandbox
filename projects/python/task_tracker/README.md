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
# Example

```
(.venv) carroyo@MacBook-Pro task_tracker $ python3 task_cli.py add "groceries"    
Successfully created task with ID 0
(.venv) carroyo@MacBook-Pro task_tracker $ python3 task_cli.py add "laundry"      
Successfully created task with ID 1
(.venv) carroyo@MacBook-Pro task_tracker $ python3 task_cli.py list           
Task ID: 0
description: groceries
status: todo
createdAt: 2025-11-30 16:55:41
updatedAt: 2025-11-30 16:55:41

Task ID: 1
description: laundry
status: todo
createdAt: 2025-11-30 16:55:49
updatedAt: 2025-11-30 16:55:49

(.venv) carroyo@MacBook-Pro task_tracker $ python3 task_cli.py mark-done 0
(.venv) carroyo@MacBook-Pro task_tracker $ python3 task_cli.py list done    
Task ID: 0
description: groceries
status: done
createdAt: 2025-11-30 16:55:41
updatedAt: 2025-11-30 16:55:41

(.venv) carroyo@MacBook-Pro task_tracker $ python3 task_cli.py delete 0
Successfully removed task with task ID 0
(.venv) carroyo@MacBook-Pro task_tracker $ python3 task_cli.py list       
Task ID: 0
description: laundry
status: todo
createdAt: 2025-11-30 16:55:49
updatedAt: 2025-11-30 16:55:49

(.venv) carroyo@MacBook-Pro task_tracker $ 
```