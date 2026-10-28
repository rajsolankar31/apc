import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("sample.txt") as f:
    for i, line in enumerate(f, 1):
        print(f"Line {i}: {line.rstrip()}")
