import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import string
words = [w.strip(string.punctuation) for w in open("sample.txt").read().split()]
longest = max(words, key=len)
print("Longest word:", longest, f"({len(longest)} letters)")
