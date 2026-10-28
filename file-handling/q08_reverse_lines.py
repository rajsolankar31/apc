import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("sample.txt") as f:
    for line in reversed(f.readlines()):
        print(line.rstrip())
