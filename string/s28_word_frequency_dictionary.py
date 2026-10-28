import string
freq = {}
for w in input("Enter a paragraph: ").lower().split():
    w = w.strip(string.punctuation)
    if w: freq[w] = freq.get(w, 0) + 1
print(freq)
