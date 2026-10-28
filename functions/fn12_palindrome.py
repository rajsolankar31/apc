def is_palindrome(x):
    s = str(x).replace(" ", "").lower(); return s == s[::-1]
v = input("Enter a string or number: "); print("Palindrome" if is_palindrome(v) else "Not a palindrome")
