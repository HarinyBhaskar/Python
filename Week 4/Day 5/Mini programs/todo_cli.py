# todo_cli.py
import argparse
import os

FILE = "todo.txt"

def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List CLI")
    parser.add_argument("action", choices=["add", "list", "clear"], help="Action to perform")
    parser.add_argument("--task", type=str, help="Task description (for add action)")
    args = parser.parse_args()

    if args.action == "add":
        if args.task:
            with open(FILE, "a") as f:
                f.write(args.task + "\n")
            print(f"Task added: {args.task}")
        else:
            print("Please provide a task with --task")
    elif args.action == "list":
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                tasks = f.readlines()
            if tasks:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("No tasks yet!")
        else:
            print("No tasks file found!")
    elif args.action == "clear":
        if os.path.exists(FILE):
            os.remove(FILE)
            print("All tasks cleared!")
        else:
            print("No tasks to clear.")

if __name__ == "__main__":
    main()
