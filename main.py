import sys
from storage import load_tasks
import task_manager

def list_tasks(status=None):
    """
    Lists tasks, optionally filtering by status (todo, in-progress, done).
    """
    tasks = load_tasks()
    
    if status:
        status = status.lower()
        if status not in ['todo', 'in-progress', 'done']:
            print(f"Error: Invalid status filter '{status}'. Choose from 'todo', 'in-progress', 'done'.")
            return
        filtered_tasks = [t for t in tasks if t['status'] == status]
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        if status:
            print(f"No tasks found with status '{status}'.")
        else:
            print("No tasks found. Use 'add' command to create a task.")
        return

    # Print the tasks in a clean tabular view
    print(f"\n{'ID':<5} | {'Description':<40} | {'Status':<12} | {'Created At':<20} | {'Updated At':<20}")
    print("-" * 107)
    
    for task in filtered_tasks:
        # Parse timestamp to clean format for presentation
        created_dt = task.get('createdAt', '').replace('T', ' ')[:19]
        updated_dt = task.get('updatedAt', '').replace('T', ' ')[:19]
        
        # Truncate description if too long
        desc = task.get('description', '')
        if len(desc) > 37:
            desc = desc[:34] + "..."
            
        print(f"{task.get('id'):<5} | {desc:<40} | {task.get('status'):<12} | {created_dt:<20} | {updated_dt:<20}")
    print()

def print_usage():
    """
    Prints how to use the CLI tool.
    """
    print("\nTask Tracker CLI Usage:")
    print("  python main.py add \"<description>\"            Add a new task")
    print("  python main.py update <id> \"<description>\"    Update a task's description")
    print("  python main.py delete <id>                    Delete a task")
    print("  python main.py mark-in-progress <id>          Mark a task as in-progress")
    print("  python main.py mark-done <id>                 Mark a task as done")
    print("  python main.py list                           List all tasks")
    print("  python main.py list <status>                  List tasks filtered by status (todo, in-progress, done)")
    print()

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing description. Usage: python main.py add \"<description>\"")
            sys.exit(1)
        description = sys.argv[2]
        new_task = task_manager.add_task(description)
        if new_task:
            print(f"Task added successfully (ID: {new_task['id']})")

    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Missing arguments. Usage: python main.py update <id> \"<description>\"")
            sys.exit(1)
        task_id = sys.argv[2]
        description = sys.argv[3]
        if task_manager.update_task(task_id, description):
            print(f"Task {task_id} updated successfully")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Missing task ID. Usage: python main.py delete <id>")
            sys.exit(1)
        task_id = sys.argv[2]
        if task_manager.delete_task(task_id):
            print(f"Task {task_id} deleted successfully")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Missing task ID. Usage: python main.py mark-done <id>")
            sys.exit(1)
        task_id = sys.argv[2]
        if task_manager.mark_done(task_id):
            print(f"Task {task_id} marked as done")

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Missing task ID. Usage: python main.py mark-in-progress <id>")
            sys.exit(1)
        task_id = sys.argv[2]
        if task_manager.mark_in_progress(task_id):
            print(f"Task {task_id} marked as in-progress")

    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)

    else:
        print(f"Error: Unknown command '{command}'")
        print_usage()
        sys.exit(1)

if __name__ == "__main__":
    main()
