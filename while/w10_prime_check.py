n = int(input("Enter a number: ")); i = 2; prime = n > 1
while i * i <= n:
    if n % i == 0: prime = False; break
    i += 1
print("Prime" if prime else "Not prime")
