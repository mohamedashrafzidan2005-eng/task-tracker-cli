import json
import os

FILE_NAME = "tasks.json"


def create_database():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)


def load_tasks():
    create_database()
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    create_database()
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)