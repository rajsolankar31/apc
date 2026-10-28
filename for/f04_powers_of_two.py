# Prints 1 2 4 8 16 32 ... 2^n  (assumed: the last term is 2 raised to n)
n = int(input("Enter n: "))
for i in range(n + 1): print(2 ** i, end=" ")
print()
