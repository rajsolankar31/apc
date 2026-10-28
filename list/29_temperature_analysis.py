# Program 29: Store temperature of 30 days and determine statistics

temperatures = []
total_days = 30

print(f"Enter temperature for {total_days} days (in °C):")
for i in range(total_days):
    temp = float(input(f"Enter temperature for Day {i+1}: "))
    temperatures.append(temp)

hottest_temp = max(temperatures)
coldest_temp = min(temperatures)
hottest_day = temperatures.index(hottest_temp) + 1
coldest_day = temperatures.index(coldest_temp) + 1

avg_temp = sum(temperatures) / total_days

days_above_avg = 0
days_below_avg = 0

for temp in temperatures:
    if temp > avg_temp:
        days_above_avg += 1
    elif temp < avg_temp:
        days_below_avg += 1

print("\n--- 30-Day Temperature Analysis ---")
print("Recorded Temperatures:", temperatures)
print(f"Hottest Day: Day {hottest_day} with {hottest_temp}°C")
print(f"Coldest Day: Day {coldest_day} with {coldest_temp}°C")
print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Days above average temperature: {days_above_avg}")
print(f"Days below average temperature: {days_below_avg}")
