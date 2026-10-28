freq = {}
for ch in input("Enter a string: "): freq[ch] = freq.get(ch, 0) + 1
for k, v in freq.items(): print(repr(k), "->", v)
