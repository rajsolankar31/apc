runs = [102, 45, 67, 12, 0, 130, 55, 89, 23, 71]
print("Highest:", max(runs), "| Lowest:", min(runs), "| Total:", sum(runs), "| Average:", sum(runs) / len(runs))
print("Centuries:", sum(r >= 100 for r in runs), "| Half-centuries:", sum(50 <= r <= 99 for r in runs))
