def fibonacci(n):
    out, a, b = [], 0, 1
    for _ in range(n): out.append(a); a, b = b, a + b
    return out
print(fibonacci(int(input("How many terms: "))))
