balance = 0
history = []
def deposit(amt):
    global balance
    balance += amt; history.append(("Deposit", amt))
def withdraw(amt):
    global balance
    if amt > balance: print("Insufficient balance!"); return
    balance -= amt; history.append(("Withdrawal", amt))
def balance_enquiry(): print("Balance:", balance)
def transaction_history():
    for t, a in history: print(t, a)
while True:
    c = input("\n1.Deposit 2.Withdraw 3.Balance 4.History 5.Exit: ")
    if c == "1": deposit(float(input("Amount: ")))
    elif c == "2": withdraw(float(input("Amount: ")))
    elif c == "3": balance_enquiry()
    elif c == "4": transaction_history()
    elif c == "5": break
