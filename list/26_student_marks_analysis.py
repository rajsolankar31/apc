# Program 26: Store marks of 20 students in a list and determine statistics

marks = []
total_students = 20

print(f"Enter marks for {total_students} students:")
for i in range(total_students):
    m = float(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

highest = marks[0]
lowest = marks[0]
total = 0

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    total += m

average = total / total_students

above_average = 0
below_average = 0

for m in marks:
    if m > average:
        above_average += 1
    elif m < average:
        below_average += 1

print("\n--- Marks Report ---")
print("Marks List:", marks)
print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")
print(f"Average marks: {average:.2f}")
print(f"Students scoring above average: {above_average}")
print(f"Students scoring below average: {below_average}")
