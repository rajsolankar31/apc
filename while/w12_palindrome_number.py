n = int(input("Enter a number: ")); t = n; r = 0
while t > 0: r = r * 10 + t % 10; t //= 10
print("Palindrome" if r == n else "Not a palindrome")
