s = input("Enter a string: "); freq = {}
for ch in s: freq[ch] = freq.get(ch, 0) + 1
m = max(freq, key=freq.get)
print(f"Most frequent: '{m}' ({freq[m]} times)")
