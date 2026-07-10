from datetime import datetime
from storage import load_tasks, save_tasks

def get_next_id(tasks):
    """
    Generates the next task ID based on the current tasks.
    """
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(description):
    """
    Adds a new task with status 'todo' and timestamps.
    """
    if not description or not description.strip():
        print("Error: Task description cannot be empty.")
        return None
        
    tasks = load_tasks()
    next_id = get_next_id(tasks)
    now = datetime.now().isoformat()
    
    new_task = {
        "id": next_id,
        "description": description.strip(),
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

def update_task(task_id, description):
    """
    Updates the description and updatedAt timestamp of a task.
    """
    if not description or not description.strip():
        print("Error: Task description cannot be empty.")
        return False
        
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be an integer.")
        return False

    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description.strip()
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            return True
            
    print(f"Error: Task with ID {task_id} not found.")
    return False

def delete_task(task_id):
    """
    Deletes a task by its ID.
    """
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be an integer.")
        return False

    tasks = load_tasks()
    original_len = len(tasks)
    tasks = [t for t in tasks if t['id'] != task_id]
    
    if len(tasks) == original_len:
        print(f"Error: Task with ID {task_id} not found.")
        return False
        
    save_tasks(tasks)
    return True

def mark_done(task_id):
    """
    Marks a task's status as 'done'.
    """
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be an integer.")
        return False

    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            return True
            
    print(f"Error: Task with ID {task_id} not found.")
    return False

def mark_in_progress(task_id):
    """
    Marks a task's status as 'in-progress'.
    """
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: Task ID must be an integer.")
        return False

    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            return True
            
    print(f"Error: Task with ID {task_id} not found.")
    return False
