products = [("Pen", 10, 50), ("Laptop", 55000, 2), ("Mouse", 800, 10), ("Keyboard", 1500, 5), ("Bag", 1200, 3)]
total_value = lambda p: p[1] * p[2]
print("a) Total value:", [(p[0], total_value(p)) for p in map(lambda p: p, products)])
print("b) Costing more than Rs.1,000:", [p[0] for p in filter(lambda p: p[1] > 1000, products)])
print("c) Sorted by total value:", [(p[0], total_value(p)) for p in sorted(products, key=total_value)])
