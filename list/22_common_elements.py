# Program 22: Find common elements between two lists

list1 = []
n1 = int(input("Enter number of elements for List 1: "))
for i in range(n1):
    val = input(f"Enter element {i+1} for List 1: ")
    list1.append(val)

list2 = []
n2 = int(input("Enter number of elements for List 2: "))
for i in range(n2):
    val = input(f"Enter element {i+1} for List 2: ")
    list2.append(val)

common_elements = []
for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)

print("\nList 1:", list1)
print("List 2:", list2)
print("Common elements:", common_elements)
