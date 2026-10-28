# cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...   (x in radians)
x = float(input("Enter x (radians): ")); n = int(input("Number of terms: "))
total = 0
for i in range(n):
    fact = 1
    for j in range(2, 2 * i + 1): fact *= j
    total += (-1) ** i * x ** (2 * i) / fact
print("cos(x) =", total)
import math; print("math.cos(x) =", math.cos(x))
