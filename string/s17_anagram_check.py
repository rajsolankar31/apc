a = input("First string: ").replace(" ", "").lower(); b = input("Second string: ").replace(" ", "").lower()
print("Anagrams" if sorted(a) == sorted(b) else "Not anagrams")
