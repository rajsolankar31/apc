s = input("Enter a string: "); r = ""
for ch in s: r = ch + r
print("Palindrome" if s == r else "Not a palindrome")
