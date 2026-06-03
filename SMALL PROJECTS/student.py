tasks = []

while True:
    task = input("Enter task (or 'quit'): ")

    if task.lower() == "quit":
        break

    tasks.append(task)

print("\nYour Tasks:")
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")