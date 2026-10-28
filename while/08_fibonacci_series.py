# Program 8: Print Fibonacci series up to n using while loop

n = int(input("Enter the value of n: "))

a, b = 0, 1
print(f"Fibonacci series up to {n}:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print()
