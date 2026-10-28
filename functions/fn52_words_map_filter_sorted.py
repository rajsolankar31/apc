words = ["python", "is", "powerful", "and", "simple", "to", "learn"]
print("a) Lengths:", list(map(lambda w: len(w), words)))
print("b) More than 5 characters:", list(filter(lambda w: len(w) > 5, words)))
print("c) Sorted by length:", sorted(words, key=lambda w: len(w)))
