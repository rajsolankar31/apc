out = ""
for ch in input("Enter a string: "):
    if ch not in out: out += ch
print("Result:", out)
