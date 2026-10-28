# Program 16: Nested List - Student Details
# Create a nested list storing student name, roll number, marks

students = []
n = int(input("How many students? "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    roll = int(input(f"Enter roll number of {name}: "))
    marks = float(input(f"Enter marks of {name}: "))
    students.append([name, roll, marks])
print("\n--- Student Details ---")
print(f"{'Name':<15} {'Roll No':<10} {'Marks':<10}")
print("-" * 35)
for student in students:
    print(f"{student[0]:<15} {student[1]:<10} {student[2]:<10}")
