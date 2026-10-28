import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import csv
rows = list(csv.DictReader(open("transactions.txt")))
dep = sum(float(r["Amount"]) for r in rows if r["Type"].lower() == "deposit")
wd = sum(float(r["Amount"]) for r in rows if r["Type"].lower() == "withdrawal")
big = max(rows, key=lambda r: float(r["Amount"]))
print("Total deposits:", dep); print("Total withdrawals:", wd)
print("Final balance:", dep - wd)
print("Largest transaction:", big["Type"], big["Amount"])
