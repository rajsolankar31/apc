# Program 4: Print sum of natural numbers up to n using while loop

n = int(input("Enter the value of n: "))

i = 1
total = 0
while i <= n:
    total += i
    i += 1

print(f"Sum of natural numbers from 1 to {n} = {total}")
