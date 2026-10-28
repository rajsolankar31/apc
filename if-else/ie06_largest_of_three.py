a, b, c = (float(input(f"Number {i}: ")) for i in (1, 2, 3))
if a >= b and a >= c: print("Largest:", a)
elif b >= c: print("Largest:", b)
else: print("Largest:", c)
