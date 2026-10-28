lst = input("Enter elements: ").split(); freq = {}
for x in lst: freq[x] = freq.get(x, 0) + 1
for k, v in freq.items(): print(k, "->", v)
