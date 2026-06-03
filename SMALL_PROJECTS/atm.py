balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Deposit amount: "))
        balance += amount

    elif choice == "3":
        amount = float(input("Withdraw amount: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds")

    elif choice == "4":
        break