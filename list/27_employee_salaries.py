# Program 27: Store salaries of employees and determine statistics

salaries = []
n = int(input("Enter number of employees: "))

for i in range(n):
    s = float(input(f"Enter salary of employee {i+1} (in ₹): "))
    salaries.append(s)

if salaries:
    highest = max(salaries)
    lowest = min(salaries)
    average = sum(salaries) / len(salaries)

    above_50k = 0
    below_30k = 0

    for s in salaries:
        if s > 50000:
            above_50k += 1
        if s < 30000:
            below_30k += 1

    print("\n--- Employee Salaries Report ---")
    print("Salaries:", salaries)
    print(f"Highest salary: ₹{highest:.2f}")
    print(f"Lowest salary: ₹{lowest:.2f}")
    print(f"Average salary: ₹{average:.2f}")
    print(f"Employees earning above ₹50,000: {above_50k}")
    print(f"Employees earning below ₹30,000: {below_30k}")
else:
    print("No employee data entered.")
