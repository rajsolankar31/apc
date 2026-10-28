import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("sample.txt") as f:
    print("Total lines:", sum(1 for _ in f))
