def shift(text, k):
    out = ""
    for c in text:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            out += chr((ord(c) - base + k) % 26 + base)
        else: out += c
    return out
t = input("Enter message: "); k = int(input("Shift key: "))
enc = shift(t, k); print("Encrypted:", enc); print("Decrypted:", shift(enc, -k))
