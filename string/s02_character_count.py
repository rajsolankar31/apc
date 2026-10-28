s = input("Enter a string: ")
v = c = d = sp = o = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou": v += 1
        else: c += 1
    elif ch.isdigit(): d += 1
    elif ch == " ": sp += 1
    else: o += 1
print(f"Vowels: {v}\nConsonants: {c}\nDigits: {d}\nSpaces: {sp}\nSpecial characters: {o}")
