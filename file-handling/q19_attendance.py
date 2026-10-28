import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import csv
for r in csv.DictReader(open("attendance.txt")):
    pct = int(r["Attended"]) / int(r["TotalClasses"]) * 100
    print(f"{r['Name']}: {pct:.1f}%" + ("  <-- below 75%" if pct < 75 else ""))
