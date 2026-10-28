s = input("Enter a string: "); old = input("Character to replace: "); new = input("Replace with: ")
out = ""
for ch in s: out += new if ch == old else ch
print("Result:", out)
