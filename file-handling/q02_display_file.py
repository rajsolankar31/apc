import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("sample.txt") as f:
    print(f.read())
