def largest(nums):
    big = nums[0]
    for n in nums:
        if n > big: big = n
    return big
print("Largest:", largest([float(x) for x in input("Enter numbers: ").split()]))
