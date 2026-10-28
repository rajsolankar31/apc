nums = [12, 7, 9, 22, 35, 40, 51, 6, 18, 77, 3, 64, 29, 10, 81]
even = sum(1 for n in nums if n % 2 == 0)
print("Even:", even, "| Odd:", len(nums) - even)
