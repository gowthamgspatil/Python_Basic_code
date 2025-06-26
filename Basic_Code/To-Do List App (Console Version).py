tasks = []

while True:
    action = input("Add/View/Exit: ").lower()
    if action == "add":
        task = input("Enter task: ")
        tasks.append(task)
    elif action == "view":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif action == "exit":
        break