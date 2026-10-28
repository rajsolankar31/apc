nums = [int(x) for x in input("Enter numbers: ").split()]
big = small = nums[0]
for n in nums:
    if n > big: big = n
    if n < small: small = n
print("Largest:", big, "| Smallest:", small)
