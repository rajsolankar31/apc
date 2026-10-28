import student
name = input("Student name: ")
marks = [float(m) for m in input("Enter marks (space separated): ").split()]
p = student.percentage(marks)
print(f"Name: {name}\nTotal: {student.total_marks(marks)}\nPercentage: {p:.2f}%\nGrade: {student.grade(p)}")
