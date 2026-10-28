ch = input("Enter a character: ").lower()
if len(ch) != 1 or not ch.isalpha(): print("Please enter a single letter")
elif ch in "aeiou": print("Vowel")
else: print("Consonant")
