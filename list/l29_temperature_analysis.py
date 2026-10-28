temps = [31, 33, 35, 36, 34, 32, 30, 29, 31, 33, 35, 37, 38, 36, 34, 33, 32, 31, 30, 29, 28, 30, 32, 34, 36, 37, 35, 33, 31, 30]
avg = sum(temps) / len(temps)
print("Hottest day: Day", temps.index(max(temps)) + 1, f"({max(temps)})")
print("Coldest day: Day", temps.index(min(temps)) + 1, f"({min(temps)})")
print("Average:", round(avg, 2))
print("Days above average:", sum(t > avg for t in temps), "| Days below average:", sum(t < avg for t in temps))
