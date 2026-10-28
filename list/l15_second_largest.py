nums = [12, 45, 2, 41, 45, 31, 10]
u = sorted(set(nums))
print("Second largest:", u[-2] if len(u) > 1 else "Not available")
