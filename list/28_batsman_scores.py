# Program 28: Store scores of a batsman in 10 matches and calculate statistics

scores = []
matches = 10

print(f"Enter scores for {matches} matches:")
for i in range(matches):
    score = int(input(f"Enter runs scored in match {i+1}: "))
    scores.append(score)

highest_score = max(scores)
lowest_score = min(scores)
total_runs = sum(scores)
average_runs = total_runs / matches

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif 50 <= score <= 99:
        half_centuries += 1

print("\n--- Batsman Performance Statistics ---")
print("Scores List:", scores)
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Total Runs: {total_runs}")
print(f"Average Runs: {average_runs:.2f}")
print(f"Number of Centuries (>= 100): {centuries}")
print(f"Number of Half-Centuries (50-99): {half_centuries}")
