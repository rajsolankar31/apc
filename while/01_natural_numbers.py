# Program 1: Print natural numbers up to n using while loop

n = int(input("Enter the value of n: "))

i = 1
print(f"Natural numbers from 1 to {n}:")
while i <= n:
    print(i, end=" ")
    i += 1
print()
