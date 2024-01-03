class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Successful deposit of", amount)
            print("New balance =", self.balance)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Successful withdrawal. New balance =", self.balance)
        elif amount > self.balance:
            print("Invalid amount")

    def get_balance(self):
        print("Current balance =", self.balance)


account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder name: ")
account_type = input("Enter account type: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(account_number, account_holder_name, account_type, initial_balance)

while True:
	print("\nMenu:")
	print("1. Deposit")
	print("2. Withdraw")
	print("3. Check Balance")
	print("4. Exit")

	choice = input("Enter your choice (1-4): ")

	if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
	elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
	elif choice == "3":
            account.get_balance()
	elif choice == "4":
            print("Exiting the program")
            break
	else:
            print("Invalid choice. Please enter a number between 1 and 4.")


