# todo.py
import logging
logging.basicConfig(filename="todo.log", level=logging.INFO)

class Todo:
    def __init__(self):
        self.tasks = []
        logging.info("New Todo created")

    def add_task(self, task):
        if not task.strip():
            logging.error("Empty task")
            raise ValueError("Task cannot be empty")
        self.tasks.append(task)
        logging.info("Added %s", task)

    def remove_task(self, task):
        if task not in self.tasks:
            logging.warning("Task not found %s", task)
            return False
        self.tasks.remove(task)
        logging.info("Removed %s", task)
        return True

if __name__ == "__main__":
    t = Todo()
    for task in input("Tasks (comma-separated): ").split(","):
        t.add_task(task.strip())
    print("Removed?", t.remove_task(input("Task to remove: ")))
