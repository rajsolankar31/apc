def count_vowels(s): return sum(c in "aeiouAEIOU" for c in s)
print("Vowels:", count_vowels(input("Enter a string: ")))
