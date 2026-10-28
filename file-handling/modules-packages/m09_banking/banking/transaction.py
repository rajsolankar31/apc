def deposit(acc, amt):
    if amt <= 0: return print("Invalid amount")
    acc["balance"] += amt
def withdraw(acc, amt):
    if amt > acc["balance"]: return print("Insufficient funds")
    acc["balance"] -= amt
