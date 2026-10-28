emps = [{"name": "Asha", "dept": "IT", "salary": 60000}, {"name": "Ravi", "dept": "HR", "salary": 45000},
        {"name": "Meena", "dept": "Finance", "salary": 52000}, {"name": "Karan", "dept": "IT", "salary": 75000}]
print("a) Earning more than Rs.50,000:", [e["name"] for e in filter(lambda e: e["salary"] > 50000, emps)])
raised = list(map(lambda e: {**e, "salary": e["salary"] * 1.10}, emps))
print("b) After 10% increase:", [(e["name"], round(e["salary"])) for e in raised])
print("c) Sorted by salary:", [(e["name"], e["salary"]) for e in sorted(emps, key=lambda e: e["salary"])])
