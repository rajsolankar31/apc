marks = [78, 85, 92, 45, 67, 88, 73, 59, 95, 81, 64, 70, 38, 90, 76, 82, 55, 68, 99, 61]
avg = sum(marks) / len(marks)
print("Highest:", max(marks), "| Lowest:", min(marks), "| Average:", avg)
print("Above average:", sum(m > avg for m in marks), "| Below average:", sum(m < avg for m in marks))
