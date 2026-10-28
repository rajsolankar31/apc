class BankAccount:
    _counter = 1000

    def __init__(self, account_holder):
        BankAccount._counter += 1
        self.account_holder = account_holder
        self.balance = 0
        self.account_number = BankAccount._counter

    def deposit(self, amount):
        if amount <= 0:
            print("Error: deposit must be positive."); return
        self.balance += amount
        print(f"Deposited {amount}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}.")

    def display_balance(self):
        print(f"{self.account_holder} (A/C {self.account_number}) balance: {self.balance}")

    def transfer(self, amount, other_account):
        if amount > self.balance:
            print("Error: insufficient funds for transfer.")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred {amount} to {other_account.account_holder}.")

a = BankAccount("Amit"); b = BankAccount("Priya")
a.deposit(5000); b.deposit(2000)
a.withdraw(1000); a.withdraw(9999)
a.transfer(1500, b); a.transfer(9999, b)
a.display_balance(); b.display_balance()
