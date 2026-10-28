def to_binary(n): return "0" if n == 0 else "1" if n == 1 else to_binary(n // 2) + str(n % 2)
print("Binary:", to_binary(int(input("Enter a decimal number: "))))
