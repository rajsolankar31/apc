students = [
    {"name": "Amit", "roll": 101, "marks": [85, 90, 78, 88, 92]},
    {"name": "Priya", "roll": 102, "marks": [92, 95, 89, 94, 98]},
    {"name": "Rahul", "roll": 103, "marks": [55, 62, 48, 70, 58]},
]
def total(s): return sum(s["marks"])
def percentage(s): return total(s) / len(s["marks"])
def grade(p): return "A" if p >= 80 else "B" if p >= 60 else "C" if p >= 40 else "F"
def class_average(sts): return sum(percentage(s) for s in sts) / len(sts)
def highest(sts): return max(sts, key=total)
def lowest(sts): return min(sts, key=total)
for s in students:
    print(f"{s['name']} (Roll {s['roll']}): Total {total(s)}, {percentage(s):.1f}%, Grade {grade(percentage(s))}")
print(f"Class average: {class_average(students):.1f}%")
print("Highest scorer:", highest(students)["name"]); print("Lowest scorer:", lowest(students)["name"])
