def save_note():
    name = input("Enter your name: ")
    note  = input ("Enter a  note: ")


    try: 
        with open ("students.txt", "a") as file:
            file.write(name + ": " + note + "\n")
        print("Notee saved succesfully")


    except Exception as e:
        print("Error saving the note", e)

#function to read notes 

def read_notes():
    try:
        with open("students.txt", "r") as file:
            print("\nsaved notes:\n")
            print(file.read())


    except FileNotFoundError:
         print("No notes found yet!")


def menu():
    while True:
        print("\n1. Save Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            save_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
        


menu()