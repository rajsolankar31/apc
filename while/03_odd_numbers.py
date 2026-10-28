# Program 3: Print odd numbers up to n using while loop

n = int(input("Enter the value of n: "))

i = 1
print(f"Odd numbers from 1 to {n}:")
while i <= n:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
print()
