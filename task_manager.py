import datetime
from storage import load_tasks, save_tasks

def get_next_id():
    tasks = load_tasks()
    if not tasks:
        return 1
    max_id = max(task["id"] for task in tasks)
    return max_id + 1

def find_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None
def add_task(description):
    tasks = load_tasks()
    new_id = get_next_id()
    now = datetime.datetime.now().isoformat()
    
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    return new_id

def update_task(task_id, description):
    tasks = load_tasks()
    task_found = False
    
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.datetime.now().isoformat()
            task_found = True
            break
            
    if task_found:
        save_tasks(tasks)
        return True
    return False
def delete_task(task_id):
    tasks = load_tasks()
    initial_length = len(tasks)
    
    tasks = [task for task in tasks if task["id"] != task_id]
    
    if len(tasks) < initial_length:
        save_tasks(tasks)
        return True
    return False

def mark_done(task_id):
    tasks = load_tasks()
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.datetime.now().isoformat()
            task_found = True
            break
            
    if task_found:
        save_tasks(tasks)
        return True
    return False

def mark_in_progress(task_id):
    tasks = load_tasks()
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.datetime.now().isoformat()
            task_found = True
            break
    if task_found:
        save_tasks(tasks)
        return True
    return False
