# Program 5: Create a list of student names. Remove first, last, and a specific student

students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
print("Original list:", students)

students.pop(0)
print("After removing first student:", students)

students.pop(-1)
print("After removing last student:", students)

name = input("Enter name of student to remove: ")
if name in students:
    students.remove(name)
    print(f"After removing {name}:", students)
else:
    print(f"{name} not found in list.")

print("Remaining students:", students)
