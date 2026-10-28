# Program 12: Repeated row number triangle
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5   (for n=5)

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
