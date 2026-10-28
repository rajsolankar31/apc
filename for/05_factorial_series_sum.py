# Program 5: Sum the sequence 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!

n = int(input("Enter the value of n: "))

factorial = 1
total = 1  # first term is 1

for i in range(1, n + 1):
    factorial *= i
    total += 1 / factorial

print(f"Sum of the series up to {n} terms: {total}")
