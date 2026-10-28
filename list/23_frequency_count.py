# Program 23: Count the frequency of each element in a list

numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = input(f"Enter element {i+1}: ")
    numbers.append(val)

frequency = {}
for item in numbers:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("\nOriginal List:", numbers)
print("Element Frequencies:")
for key, count in frequency.items():
    print(f"'{key}': {count} time(s)")
