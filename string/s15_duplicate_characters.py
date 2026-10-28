s = input("Enter a string: "); dup = []
for ch in s:
    if s.count(ch) > 1 and ch not in dup: dup.append(ch)
print("Duplicate characters:", dup)
