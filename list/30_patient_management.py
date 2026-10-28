# Program 30: Store patient names and ages using lists

patient_names = []
patient_ages = []

while True:
    print("\n--- Hospital Patient Management ---")
    print("1. Add a patient")
    print("2. Delete a patient")
    print("3. Search a patient")
    print("4. Display all patients")
    print("5. Count total patients")
    print("6. Exit")

    choice = input("Enter choice (1-6): ").strip()

    if choice == "1":
        name = input("Enter patient name: ").strip()
        age = int(input("Enter patient age: "))
        patient_names.append(name)
        patient_ages.append(age)
        print(f"Patient '{name}' added successfully.")

    elif choice == "2":
        name = input("Enter patient name to delete: ").strip()
        if name in patient_names:
            idx = patient_names.index(name)
            patient_names.pop(idx)
            patient_ages.pop(idx)
            print(f"Patient '{name}' deleted successfully.")
        else:
            print(f"Patient '{name}' not found.")

    elif choice == "3":
        name = input("Enter patient name to search: ").strip()
        if name in patient_names:
            idx = patient_names.index(name)
            print(f"Patient found: {patient_names[idx]}, Age: {patient_ages[idx]}")
        else:
            print(f"Patient '{name}' not found.")

    elif choice == "4":
        if patient_names:
            print("\nList of Patients:")
            for i in range(len(patient_names)):
                print(f"{i+1}. Name: {patient_names[i]}, Age: {patient_ages[i]}")
        else:
            print("No patients in the list.")

    elif choice == "5":
        print(f"Total registered patients: {len(patient_names)}")

    elif choice == "6":
        print("Exiting patient management system.")
        break
    else:
        print("Invalid choice, please select between 1 and 6.")
