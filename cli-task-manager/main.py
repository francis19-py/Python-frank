import json
tasks = []
next_id = 1

def add_tasks():
    global next_id
    title = input("Enter the task title: ")

    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    next_id += 1
    print("task completed successfully ")

def list_tasks():
    if not tasks:
        print("NO tasks available ")
        return
    print("/n -----------your tasks----------------")

    for task in tasks:
            if task ["completed"]:
                status = "Completed"
            else:
                status = "Pending"
            print(f"ID: {task['id']} | Title: {task['title']} | Status: {status}")

def update_task():
    try:
        task_id = int(input("Enter the task id to update: "))
    except ValueError:
        print("please enter a valid integer for the task")
        return
    for task in tasks:
        if task["id"] == task_id:
            new_title = input ("Enter the new task title: ").strip()

            if not new_title:
                print("task title cannot be empty")
                return
    task["title"] = new_title
    print("task updated successfully")
    return
    print("task not found !")

def mark_as_complete():
    try:
        task_id = int (input("Enter the task id to mark as complete: "))
    except ValueError:
        print("Please enter a valid integer: ")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("Task completed ")
            return
    print("task not found !")

def delete_task():
    try:
        task_id = int(input("Enter the task id to delete: "))
    except ValueError:
        print("Please enter a valid integer for the task id.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted successfully.")
            return
    print("Task not found!")   

def save_tasks():
    with open ("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved successsfully !") 

def load_tasks():
    global tasks, next_id

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            if tasks:
                next_id = max(task["id"] for task in tasks) + 1
            else:
                next_id = 1

            print ("Tasks loaded successfully!")

    except FileNotFoundError:
        print("no saved tasks found. starting fresh...")


while True:
    print("/n ======================")
    print("    CLI TASK MANAGER")
    print("======================")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. update a  Task")
    print("4. mark a task as complete")
    print("5. Delete a Task")
    print("6. save tasks")
    print("7. Exit")

    choice = input("choose an option")
    if choice == "1":
        add_tasks()
    elif  choice == "2":
        list_tasks()
    elif choice == "3":
        update_task()    
    elif  choice == "4":
        mark_as_complete()
    elif choice == "5":
        delete_task() 
    elif choice == "6":
        save_tasks()
    elif  choice == "7":
        print("Exiting the program...")
        break
    else:
        print("The feature is not ready yet. Please choose another option.")

