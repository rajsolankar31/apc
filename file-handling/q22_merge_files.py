import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("merged.txt", "w") as out:
    for name in ("file1.txt", "file2.txt"):
        out.write(open(name).read())
print(open("merged.txt").read())
