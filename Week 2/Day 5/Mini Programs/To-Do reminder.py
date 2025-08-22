from datetime import datetime, timedelta

tasks = [
    {"task": "Submit project", "days": 2},
    {"task": "Pay bill", "days": 5},
    {"task": "Meeting", "days": 1},
]

print("To-Do List with Deadlines:\n")
for t in tasks:
    due_date = datetime.now() + timedelta(days=t["days"])
    print(f"{t['task']} → Due by {due_date.strftime('%d-%m-%Y')}")
