# Program 6: Compute cosine series
# cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ... x^n/n!

import math

x = float(input("Enter the value of x (in degrees): "))
n = int(input("Enter the number of terms: "))

x = math.radians(x)  # convert degrees to radians

cos_value = 0
for i in range(n):
    power = 2 * i
    sign = (-1) ** i
    cos_value += sign * (x ** power) / math.factorial(power)

print(f"Computed cos(x) = {cos_value}")
print(f"Built-in  cos(x) = {math.cos(x)}")
