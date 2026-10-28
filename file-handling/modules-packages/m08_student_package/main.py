from student import marks, grade, attendance
name = input("Name: ")
m = [float(x) for x in input("Marks (space separated): ").split()]
att, tot = int(input("Classes attended: ")), int(input("Total classes: "))
p = marks.percentage(m)
print(f"\n--- Report: {name} ---\nTotal: {marks.total(m)}\nPercentage: {p:.2f}%\nGrade: {grade.calculate_grade(p)}")
print("Attendance:", f"{att/tot*100:.1f}%", "| Eligible:", "Yes" if attendance.is_eligible(att, tot) else "No")
