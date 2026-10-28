lst = [4, 2, 4, 1, 2, 5, 1]; out = []
for x in lst:
    if x not in out: out.append(x)
print("Original:", lst); print("Without duplicates:", out)
