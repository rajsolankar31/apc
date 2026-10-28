# Program 9: Increasing alphabet triangle
# A
# A B
# A B C
# A B C D
# A B C D E   (for n=5)

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
