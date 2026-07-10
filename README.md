# Task Tracker CLI

## Software Design Document (SDD)

---

# 1. Objective

Develop a modular Command Line Interface (CLI) application in Python for managing tasks.

The application must persist data using a local JSON file without external libraries or databases.

The system architecture is divided into three independent modules to allow parallel development.

---

# 2. System Architecture

```
                    User
                      │
                      ▼
          +----------------------+
          |      main.py         |
          | Command Line Layer   |
          +----------------------+
                      │
                      ▼
          +----------------------+
          |  task_manager.py     |
          | Business Logic Layer |
          +----------------------+
                      │
                      ▼
          +----------------------+
          |    storage.py        |
          |   Data Access Layer  |
          +----------------------+
                      │
                      ▼
                tasks.json
```

Each module is responsible for exactly one layer.

No module should bypass another layer.

Example:

❌ main.py → tasks.json

✅ main.py → task_manager.py → storage.py → tasks.json

---

# 3. Project Directory

```
task-tracker-cli/

│

├── main.py

├── task_manager.py

├── storage.py

├── tasks.json

└── README.md
```

---

# 4. Data Model

Each task is represented as a dictionary.

```
{
    "id": Integer,
    "description": String,
    "status": "todo | in-progress | done",
    "createdAt": String,
    "updatedAt": String
}
```

The JSON file stores a list of tasks.

```
[
    Task,
    Task,
    Task
]
```

---

# 5. Module Specifications

---

# Module 1 — Storage Layer

**Developer:** Sama

## File

```
storage.py
```

## Purpose

Implements all file operations.

No business logic is allowed inside this module.

It should never:

- Generate task IDs
- Update task status
- Validate commands

It only reads and writes data.

---

## Required Functions

```
create_database()

load_tasks()

save_tasks(tasks)
```

---

## Responsibilities

### create_database()

Check whether

```
tasks.json
```

exists.

If not:

Create it.

Initialize it with

```
[]
```

---

### load_tasks()

Read

```
tasks.json
```

Return

```
list[dict]
```

If an error occurs:

Return an empty list.

---

### save_tasks(tasks)

Receive

```
list[dict]
```

Convert to JSON.

Overwrite

```
tasks.json
```

---

## Output Contract

Always returns

```
list[dict]
```

---

# Module 2 — Business Logic

**Developer:** Yahia

## File

```
task_manager.py
```

## Purpose

Contains every operation performed on tasks.

This module communicates only with

```
storage.py
```

Never with the user.

---

## Required Functions

```
get_next_id()

find_task(id)

add_task(description)

update_task(id, description)

delete_task(id)

mark_done(id)

mark_in_progress(id)
```

---

## Function Flow

Example:

```
add_task()

↓

load_tasks()

↓

append()

↓

save_tasks()

↓

return success
```

---

## Rules

IDs are unique.

IDs never change.

Deleted IDs are NOT reused.

Status values are limited to

```
todo

in-progress

done
```

---

# Module 3 — CLI Layer

**Developer:** Omar

## File

```
main.py
```

## Purpose

Acts as the application's controller.

Responsible for parsing user input.

Responsible for displaying output.

Never reads JSON directly.

---

## Required Functions

```
main()

parse_command()

list_tasks()

print_error()

print_success()
```

---

## Supported Commands

```
add

update

delete

mark-done

mark-in-progress

list
```

---

## Input Validation

Before calling Business Logic:

Check

- number of arguments

- command exists

- id is integer

- description exists

---

# 6. Communication Protocol

Storage Layer exports

```
load_tasks()

save_tasks()
```

Business Layer imports them.

Business Layer exports

```
add_task()

update_task()

delete_task()

mark_done()

mark_in_progress()
```

CLI imports them.

---

# 7. Sequence Diagram

Example

```
User

│

│ python main.py add "Study"

▼

main.py

│

│ add_task("Study")

▼

task_manager.py

│

│ load_tasks()

▼

storage.py

│

│ Read JSON

▼

tasks.json

▲

│

│ Return list

│

task_manager.py

│

│ Append task

│

│ save_tasks()

▼

storage.py

│

│ Write JSON

▼

tasks.json

▲

│

Return Success

▲

main.py

│

Print

Task Added Successfully
```

---

# 8. Git Workflow

Each member works on a dedicated branch.

```
main

├── storage

├── task-manager

└── cli
```

Development process

```
Clone

↓

Create Branch

↓

Implement Module

↓

Commit

↓

Push

↓

Pull Request

↓

Merge
```

---

# 9. Integration Order

Step 1

Storage Layer

↓

Step 2

Business Layer

↓

Step 3

CLI Layer

↓

Step 4

Testing

↓

Step 5

Final Merge

---

# 10. Testing Checklist

Storage

- Create file

- Read file

- Write file

Business

- Add

- Update

- Delete

- Change status

CLI

- Invalid command

- Missing arguments

- List commands

- Correct output

---

# 11. Constraints

✔ Python only

✔ JSON storage

✔ No external libraries

✔ Modular design

✔ Error handling

✔ Command-line arguments only

✔ Maintainable code
