import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
old = input("Word to replace: "); new = input("Replace with: ")
text = open("sample.txt").read()
with open("sample_modified.txt", "w") as f:   # new file; use "sample.txt" to overwrite
    f.write(text.replace(old, new))
print("Saved to sample_modified.txt")
print(open("sample_modified.txt").read())
