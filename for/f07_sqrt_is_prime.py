n = int(input("Enter a number: "))
r = int(n ** 0.5)
if r * r != n: print("Square root is not a whole number, so it cannot be prime")
elif r < 2: print("Square root", r, "is not prime")
else:
    for i in range(2, int(r ** 0.5) + 1):
        if r % i == 0: print("Square root", r, "is not prime"); break
    else: print("Square root", r, "is prime")
