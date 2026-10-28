import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import csv
with open("students.txt") as f:
    recs = list(csv.DictReader(f))
print("All records:")
for r in recs: print(r["RollNo"], r["Name"], r["Marks"])
top = max(recs, key=lambda r: int(r["Marks"]))
print("Highest:", top["Name"], top["Marks"])
print("Average:", sum(int(r["Marks"]) for r in recs) / len(recs))
print("Scored > 80:", [r["Name"] for r in recs if int(r["Marks"]) > 80])
