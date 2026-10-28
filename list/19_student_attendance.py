# Program 19: Student Attendance
# Store names of students present in class. Perform various operations

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
while True:
    print("\n--- Student Attendance Menu ---")
    print("1. Display total students")
    print("2. Search a student's attendance")
    print("3. Add a new student")
    print("4. Remove an absent student")
    print("5. Display all students")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"Total students present: {len(students)}")
    elif choice == 2:
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} is present.")
        else:
            print(f"{name} is absent or not in the list.")
    elif choice == 3:
        name = input("Enter new student name: ")
        students.append(name)
        print(f"{name} added.")
    elif choice == 4:
        name = input("Enter student name to remove: ")
        if name in students:
            students.remove(name)
            print(f"{name} removed.")
        else:
            print(f"{name} not found.")
    elif choice == 5:
        print("Students:", students)
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
