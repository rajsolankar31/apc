def is_pal(s):
    if len(s) <= 1: return True
    return s[0] == s[-1] and is_pal(s[1:-1])
s = input("Enter a string: ").replace(" ", "").lower(); print("Palindrome" if is_pal(s) else "Not a palindrome")
