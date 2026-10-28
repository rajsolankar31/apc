# Program 11: Find the sum of digits of a given number using while loop

num = int(input("Enter a number: "))

total = 0
temp = num
while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print(f"Sum of digits of {num} = {total}")
