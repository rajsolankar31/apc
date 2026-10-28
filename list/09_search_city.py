# Program 9: Create a list of cities and let the user search for a city

cities = ["Mumbai", "Delhi", "Pune", "Chennai", "Kolkata", "Bangalore", "Hyderabad"]
print("Cities:", cities)

search = input("Enter city name to search: ")

if search in cities:
    print(f"{search} exists in the list at index {cities.index(search)}.")
else:
    print(f"{search} does NOT exist in the list.")
