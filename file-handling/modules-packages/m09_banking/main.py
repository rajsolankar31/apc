from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import simple_interest, emi
acc = create_account(input("Account holder: "))
deposit(acc, float(input("Deposit: "))); withdraw(acc, float(input("Withdraw: ")))
print("Balance:", get_balance(acc))
print("Loan 100000 @8% for 2 yrs -> interest:", simple_interest(100000, 8, 2), "| EMI (24 mo):", round(emi(100000, 8, 24), 2))
