import subprocess
import os
import shutil

def run_cmd(args):
    print(f"Running: python main.py {' '.join(args)}")
    result = subprocess.run(
        ["python", "main.py"] + args,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    print("STDOUT:")
    print(result.stdout)
    if result.stderr:
        print("STDERR:")
        print(result.stderr)
    return result.stdout, result.stderr

def main():
    db_file = "tasks.json"
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Removed existing {db_file} to start clean.\n")
        
    print("--- 1. Add Task ---")
    run_cmd(["add", "Buy groceries"])
    
    print("--- 2. List Tasks ---")
    run_cmd(["list"])
    
    print("--- 3. Update Task ---")
    run_cmd(["update", "1", "Buy groceries and cook dinner"])
    
    print("--- 4. List Tasks after Update ---")
    run_cmd(["list"])
    
    print("--- 5. Mark In Progress ---")
    run_cmd(["mark-in-progress", "1"])
    
    print("--- 6. List In Progress ---")
    run_cmd(["list", "in-progress"])
    
    print("--- 7. Mark Done ---")
    run_cmd(["mark-done", "1"])
    
    print("--- 8. List Done ---")
    run_cmd(["list", "done"])
    
    print("--- 9. Delete Task ---")
    run_cmd(["delete", "1"])
    
    print("--- 10. List after Delete ---")
    run_cmd(["list"])

if __name__ == "__main__":
    main()
