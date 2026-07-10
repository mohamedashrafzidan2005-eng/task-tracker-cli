import os
import json

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks.json')

def load_tasks():
    """
    Loads tasks from the tasks.json file.
    If the file does not exist, it initializes and saves an empty list [].
    """
    if not os.path.exists(DB_FILE):
        try:
            save_tasks([])
            return []
        except Exception as e:
            print(f"Error initializing database file: {e}")
            return []
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error: tasks.json is corrupted (invalid JSON format). {e}")
        return []
    except PermissionError as e:
        print(f"Error: Permission denied when reading tasks.json. {e}")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """
    Saves tasks to the tasks.json file.
    """
    try:
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
    except PermissionError as e:
        print(f"Error: Permission denied when writing to tasks.json. {e}")
    except Exception as e:
        print(f"Error saving tasks: {e}")
