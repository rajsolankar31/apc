# Program 12: Check if the entered number is palindrome or not using while loop

num = int(input("Enter a number: "))

original = num
reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if original == reverse:
    print(f"{original} is a PALINDROME.")
else:
    print(f"{original} is NOT a palindrome.")
