import string_utils as su
s = input("Enter a string: ")
print("Vowels:", su.count_vowels(s)); print("Reversed:", su.reverse_string(s))
print("Palindrome:", su.is_palindrome(s)); print("Words:", su.count_words(s))
print("Without spaces:", su.remove_spaces(s))
