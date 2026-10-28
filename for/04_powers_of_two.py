# Program 4: Print powers of 2: 1 2 4 8 16 32 ... up to n terms

n = int(input("Enter the number of terms: "))

print("Series: ", end="")
for i in range(n):
    print(2 ** i, end=" ")
print()
