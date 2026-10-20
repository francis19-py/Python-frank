while True:
    print("/n ======================")
    print("    CLI TASK MANAGER")
    print("======================")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. update a  Task")
    print("4. mark a task as complete")
    print("5. Delete a Task")
    print("6. Exit")

    choice = input("choose an option")

    if choice == "6":
        print("Exiting the program...")
        break
    else:
        print("you selected option:", choice)

        