# prints the first n terms of the series
n = int(input("Number of terms: ")); a, b, count = 0, 1, 0
while count < n:
    print(a, end=" "); a, b = b, a + b; count += 1
print()
