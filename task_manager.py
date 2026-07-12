import datetime
from typing import List, Dict, Tuple, Optional, Any
from storage import load_tasks, save_tasks

def _get_current_time() -> str:
    return datetime.datetime.now().isoformat()

def _find_task_index(tasks: List[Dict[str, Any]], task_id: int) -> Optional[int]:
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return index
    return None

def get_next_id() -> int:
    tasks = load_tasks()
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def list_tasks() -> List[Dict[str, Any]]:
    return load_tasks()

def add_task(description: str) -> Tuple[bool, str]:
    tasks = load_tasks()
    new_id = get_next_id()
    now = _get_current_time()
    
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    
    return True, f"Task added successfully (ID: {new_id})"

def update_task(task_id: int, description: str) -> Tuple[bool, str]:
    tasks = load_tasks()
    index = _find_task_index(tasks, task_id)
    
    if index is None:
        return False, f"Task {task_id} not found."
        
    tasks[index]["description"] = description
    tasks[index]["updatedAt"] = _get_current_time()
    save_tasks(tasks)
    
    return True, f"Task {task_id} updated successfully."

def delete_task(task_id: int) -> Tuple[bool, str]:
    tasks = load_tasks()
    index = _find_task_index(tasks, task_id)
    
    if index is None:
        return False, f"Task {task_id} not found."
        
    tasks.pop(index)
    save_tasks(tasks)
    
    return True, f"Task {task_id} deleted successfully."

def mark_done(task_id: int) -> Tuple[bool, str]:
    tasks = load_tasks()
    index = _find_task_index(tasks, task_id)
    
    if index is None:
        return False, f"Task {task_id} not found."
        
    tasks[index]["status"] = "done"
    tasks[index]["updatedAt"] = _get_current_time()
    save_tasks(tasks)
    
    return True, f"Task {task_id} marked as done."

def mark_in_progress(task_id: int) -> Tuple[bool, str]:
    tasks = load_tasks()
    index = _find_task_index(tasks, task_id)
    
    if index is None:
        return False, f"Task {task_id} not found."
        
    tasks[index]["status"] = "in-progress"
    tasks[index]["updatedAt"] = _get_current_time()
    save_tasks(tasks)
    
    return True, f"Task {task_id} marked as in-progress."