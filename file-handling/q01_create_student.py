import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
name = input("Name: "); roll = input("Roll number: ")
branch = input("Branch: "); sem = input("Semester: ")
with open("student.txt", "w") as f:
    f.write(f"Name: {name}\nRoll No: {roll}\nBranch: {branch}\nSemester: {sem}\n")
print("student.txt created.")
