# Program 1: Print natural numbers up to n

n = int(input("Enter the value of n: "))

print(f"Natural numbers from 1 to {n}:")
for i in range(1, n + 1):
    print(i, end=" ")
print()
