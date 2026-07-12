import sys

from task_manager import (
    add_task,
    delete_task,
    list_tasks,
    mark_done,
    mark_in_progress,
    update_task,
)

SUPPORTED_COMMANDS = {
    "add",
    "update",
    "delete",
    "mark-done",
    "mark-in-progress",
    "list",
}


def _suggest_command(command):
    if not command:
        return None

    for supported in SUPPORTED_COMMANDS:
        if supported.startswith(command) or command.startswith(supported):
            return supported

    return None


def parse_command(args):
    if not args:
        return None, "No command supplied."

    command = args[0]
    if command not in SUPPORTED_COMMANDS:
        suggestion = _suggest_command(command)
        if suggestion:
            return None, f"Unsupported command: {command}. Did you mean '{suggestion}'?"
        return None, f"Unsupported command: {command}"

    if command == "list":
        if len(args) != 1:
            return None, "Usage: list"
        return {"command": command}, None

    if command == "add":
        if len(args) != 2:
            return None, "Usage: add <description>"
        return {"command": command, "description": args[1]}, None

    if command == "update":
        if len(args) != 3:
            return None, "Usage: update <id> <description>"
        try:
            task_id = int(args[1])
        except ValueError:
            return None, "id must be an integer."
        return {"command": command, "id": task_id, "description": args[2]}, None

    if command == "delete":
        if len(args) != 2:
            return None, "Usage: delete <id>"
        try:
            task_id = int(args[1])
        except ValueError:
            return None, "id must be an integer."
        return {"command": command, "id": task_id}, None

    if command in {"mark-done", "mark-in-progress"}:
        if len(args) != 2:
            return None, f"Usage: {command} <id>"
        try:
            task_id = int(args[1])
        except ValueError:
            return None, "id must be an integer."
        return {"command": command, "id": task_id}, None

    return None, "Invalid input."


def print_error(message):
    print(f"Error: {message}")


def print_success(message):
    print(message)


def list_tasks_cli():
    tasks = list_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(
            f"#{task['id']} [{task['status']}] {task['description']}"
        )


def main():
    parsed, error = parse_command(sys.argv[1:])
    if error:
        print_error(error)
        return 1

    command = parsed["command"]
    if command == "list":
        list_tasks_cli()
        return 0

    if command == "add":
        success, message = add_task(parsed["description"])
    elif command == "update":
        success, message = update_task(parsed["id"], parsed["description"])
    elif command == "delete":
        success, message = delete_task(parsed["id"])
    elif command == "mark-done":
        success, message = mark_done(parsed["id"])
    elif command == "mark-in-progress":
        success, message = mark_in_progress(parsed["id"])
    else:
        print_error("Unhandled command.")
        return 1

    if success:
        print_success(message)
    else:
        print_error(message)
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())