def count_vowels(s): return sum(c in "aeiouAEIOU" for c in s)
def reverse_string(s): return s[::-1]
def is_palindrome(s):
    s = s.replace(" ", "").lower(); return s == s[::-1]
def count_words(s): return len(s.split())
def remove_spaces(s): return s.replace(" ", "")
