# Program 5: Print sum of odd numbers up to n using while loop

n = int(input("Enter the value of n: "))

i = 1
total = 0
while i <= n:
    if i % 2 != 0:
        total += i
    i += 1

print(f"Sum of odd numbers from 1 to {n} = {total}")
