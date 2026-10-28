# Program 7: Print natural numbers up to n in reverse order using while loop

n = int(input("Enter the value of n: "))

i = n
print(f"Natural numbers from {n} to 1:")
while i >= 1:
    print(i, end=" ")
    i -= 1
print()
