cities = ["Pune", "Mumbai", "Delhi", "Chennai", "Kolkata"]
c = input("Enter city name: ").strip().title()
print(c, "exists in the list" if c in cities else "is not in the list")
