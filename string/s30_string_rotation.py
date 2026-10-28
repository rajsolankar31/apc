a = input("First string: "); b = input("Second string: ")
print("Yes" if len(a) == len(b) and b in a + a else "No")
