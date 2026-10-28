def reverse(s):
    r = ""
    for c in s: r = c + r
    return r
print(reverse(input("Enter a string: ")))
