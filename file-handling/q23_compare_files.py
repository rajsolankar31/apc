import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
a = open("file1.txt").readlines(); b = open("file3.txt").readlines()
if a == b: print("Files are identical.")
else:
    for i in range(max(len(a), len(b))):
        x = a[i] if i < len(a) else None; y = b[i] if i < len(b) else None
        if x != y:
            print(f"Files differ. First difference at line {i+1}:")
            print("File 1:", repr(x)); print("File 2:", repr(y)); break
