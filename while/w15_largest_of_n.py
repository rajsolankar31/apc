n = int(input("How many numbers: ")); i = 1
largest = float(input("Number 1: "))
while i < n:
    x = float(input(f"Number {i + 1}: ")); i += 1
    if x > largest: largest = x
print("Largest:", largest)
