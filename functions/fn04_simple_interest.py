def simple_interest(p, r, t): return p * r * t / 100
p = float(input("Principal: ")); r = float(input("Rate (%): ")); t = float(input("Time (years): "))
print("Simple interest:", simple_interest(p, r, t))
