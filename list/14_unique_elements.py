# Program 14: Unique Elements
# Create a list with duplicates and display only unique elements

numbers = [1, 2, 3, 2, 4, 5, 1, 3, 6, 7, 5, 8]
print("Original list:", numbers)
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("Unique elements:", unique)
