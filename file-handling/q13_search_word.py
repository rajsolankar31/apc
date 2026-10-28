import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import string
word = input("Word to search: ").lower()
count, lines = 0, []
for n, line in enumerate(open("sample.txt"), 1):
    c = [w.strip(string.punctuation) for w in line.lower().split()].count(word)
    if c: count += c; lines.append(n)
print(f"'{word}' occurs {count} time(s)" + (f" on line(s): {lines}" if lines else ""))
