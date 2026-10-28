import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import csv
def load():
    with open("employees.txt") as f: return list(csv.DictReader(f))
def display_all(e):
    for x in e: print(x["ID"], x["Name"], x["Department"], x["Salary"])
def highest_paid(e): return max(e, key=lambda x: int(x["Salary"]))
def average_salary(e): return sum(int(x["Salary"]) for x in e) / len(e)
def above(e, s): return [x for x in e if int(x["Salary"]) > s]
emp = load()
display_all(emp)
h = highest_paid(emp); print("Highest paid:", h["Name"], h["Salary"])
print("Average salary:", average_salary(emp))
limit = int(input("Show employees earning above: "))
for x in above(emp, limit): print(x["Name"], x["Salary"])
