# Program 8: Print the pattern
# A B C
# A B C
# A B C

n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()
