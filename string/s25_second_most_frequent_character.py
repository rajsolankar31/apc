s = input("Enter a string: "); freq = {}
for ch in s: freq[ch] = freq.get(ch, 0) + 1
counts = sorted(set(freq.values()), reverse=True)
if len(counts) < 2: print("No second most frequent character")
else: print("Second most frequent:", [(k, v) for k, v in freq.items() if v == counts[1]])
