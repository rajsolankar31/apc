import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
name = input("Name: "); roll = input("Roll number: ")
branch = input("Branch: "); sem = input("Semester: ")
with open("student.txt", "a") as f:
    f.write(f"\nName: {name}\nRoll No: {roll}\nBranch: {branch}\nSemester: {sem}\n")
print(open("student.txt").read())
