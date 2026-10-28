# 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
n = int(input("Enter n: ")); total = 1; fact = 1
for i in range(1, n + 1):
    fact *= i
    total += 1 / fact
print("Sum =", total)
