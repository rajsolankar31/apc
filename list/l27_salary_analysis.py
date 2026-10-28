sal = [25000, 48000, 52000, 75000, 29000, 61000, 35000, 28000, 90000]
print("Highest:", max(sal), "| Lowest:", min(sal), "| Average:", sum(sal) / len(sal))
print("Earning above Rs.50,000:", sum(s > 50000 for s in sal))
print("Earning below Rs.30,000:", sum(s < 30000 for s in sal))
