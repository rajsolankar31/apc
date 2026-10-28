a, b, c = (float(input(f"Number {i}: ")) for i in (1, 2, 3))
if a <= b and a <= c: print("Smallest:", a)
elif b <= c: print("Smallest:", b)
else: print("Smallest:", c)
