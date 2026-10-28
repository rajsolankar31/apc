import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("sample.txt") as f, open("sample_upper.txt", "w") as out:
    out.write(f.read().upper())
print(open("sample_upper.txt").read())
