emps = [{"name": "Asha", "salary": 60000}, {"name": "Ravi", "salary": 45000}, {"name": "Meena", "salary": 52000}]
for e in sorted(emps, key=lambda e: e["salary"]): print(e["name"], e["salary"])
