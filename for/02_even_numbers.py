# Program 2: Print even numbers up to n

n = int(input("Enter the value of n: "))

print(f"Even numbers from 1 to {n}:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()
