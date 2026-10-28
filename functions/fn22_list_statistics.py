def stats(nums): return min(nums), max(nums), sum(nums), sum(nums) / len(nums)
lo, hi, s, avg = stats([float(x) for x in input("Enter numbers: ").split()])
print(f"Minimum: {lo}\nMaximum: {hi}\nSum: {s}\nAverage: {avg}")
