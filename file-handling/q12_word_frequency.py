import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import string
freq = {}
for w in open("sample.txt").read().lower().split():
    w = w.strip(string.punctuation)
    if w: freq[w] = freq.get(w, 0) + 1
print(freq)
