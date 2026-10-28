# Program 10: Decreasing alphabet triangle
# A B C D E
# A B C D
# A B C
# A B
# A           (for n=5)

n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
