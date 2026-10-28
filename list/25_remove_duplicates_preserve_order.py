# Program 25: Remove all duplicate elements while preserving original order

items = []
n = int(input("Enter number of elements in the list: "))
for i in range(n):
    val = input(f"Enter element {i+1}: ")
    items.append(val)

print("\nOriginal list with duplicates:", items)

unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)

print("List after removing duplicates (preserving order):", unique_items)
