class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # private attribute

    def get_balance(self): return self.__balance
    def set_balance(self, amount):
        if amount < 0: print("Balance cannot be negative")
        else: self.__balance = amount

a = Account("Amit", 1000)
print(a.get_balance())
a.set_balance(-50); a.set_balance(2500)
print(a.get_balance())
try: print(a.__balance)
except AttributeError as e: print("Direct access blocked:", e)
