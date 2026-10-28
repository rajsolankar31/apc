students = [("Amit", 85), ("Priya", 92), ("Rahul", 70), ("Sneha", 78), ("Karan", 66)]
average = lambda lst: sum(m for _, m in lst) / len(lst)
print("a) Average marks:", average(students))
print("b) Scoring above 75:", list(filter(lambda s: s[1] > 75, students)))
print("c) Sorted by marks:", sorted(students, key=lambda s: s[1]))
