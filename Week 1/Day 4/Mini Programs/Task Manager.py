tasks = []

print(" Task Manager ")
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
            continue
        print("\n Your Tasks ")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
            continue
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    elif choice == "4":
        print("Goodbye! Stay productive.")
        break
    else:
        print("Invalid option.")
