def second_largest(nums):
    u = sorted(set(nums))
    return u[-2] if len(u) > 1 else None
print("Second largest:", second_largest([int(x) for x in input("Enter numbers: ").split()]))
