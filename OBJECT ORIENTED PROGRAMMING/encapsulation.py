#Encapsulation is the practice of bundling data and methods inside a class while controlling how that data is accessed or modified.
'''
Understanding public, protected and private attributes
Type	Naming	Meaning
Public	balance	Generally accessible
Protected	_balance	Intended for internal use; convention only
Private	__balance	Name-mangled to discourage direct access
'''

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter #The setter validates the new value before updating the private attribute.
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

bank_account = BankAccount(5000)
print("Initial balance",bank_account.balance)
bank_account.deposit(2000)
print("updated balance:", bank_account.balance)

bank_account.withdraw(1000)
bank_account.balance =300
print("Final balance:", bank_account.balance)