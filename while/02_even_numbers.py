# Program 2: Print even numbers up to n using while loop

n = int(input("Enter the value of n: "))

i = 1
print(f"Even numbers from 1 to {n}:")
while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()
