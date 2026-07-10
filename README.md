# Task Tracker CLI

A command-line task management application built with Python.

The application stores tasks in a JSON file and allows users to manage them directly from the terminal.

## Features

- Add tasks
- Update tasks
- Delete tasks
- Mark tasks as In Progress
- Mark tasks as Done
- List all tasks
- Filter tasks by status
- Automatic JSON file creation
- Error handling

---

## Technologies

- Python
- JSON
- Command Line Interface (CLI)

---

## Project Structure

```
task-tracker-cli/
│
├── main.py
├── storage.py
├── task_manager.py
├── tasks.json
└── README.md
```

---

## Team Roles

### Member 1 — Storage Layer

Responsible for:

- Creating `tasks.json`
- Loading tasks from JSON
- Saving tasks to JSON
- Handling file-related errors

Functions:

- `load_tasks()`
- `save_tasks()`

---

### Member 2 — Task Management Layer

Responsible for:

- Add Task
- Update Task
- Delete Task
- Mark Done
- Mark In Progress
- Generate Task IDs

Functions:

- `add_task()`
- `update_task()`
- `delete_task()`
- `mark_done()`
- `mark_in_progress()`
- `get_next_id()`

---

### Member 3 — Command Line Interface

Responsible for:

- Reading command-line arguments
- Validating commands
- Calling task functions
- Displaying output
- Listing tasks

Functions:

- `main()`
- `list_tasks()`
- Command parser

---

## Workflow

```
User
    │
    ▼
CLI (main.py)
    │
    ▼
Task Manager
    │
    ▼
Storage
    │
    ▼
tasks.json
```

---

## Example Commands

```bash
python main.py add "Buy groceries"

python main.py update 1 "Buy groceries and cook dinner"

python main.py delete 1

python main.py mark-done 1

python main.py mark-in-progress 1

python main.py list

python main.py list done

python main.py list todo

python main.py list in-progress
```

---

## Task Status

- todo
- in-progress
- done
