# Program 21: Accept two lists and merge them into a single list

list1 = []
n1 = int(input("Enter number of elements for List 1: "))
for i in range(n1):
    item = input(f"Enter element {i+1} for List 1: ")
    list1.append(item)

list2 = []
n2 = int(input("Enter number of elements for List 2: "))
for i in range(n2):
    item = input(f"Enter element {i+1} for List 2: ")
    list2.append(item)

# Merging lists using + operator
merged_list = list1 + list2

print("\nList 1:", list1)
print("List 2:", list2)
print("Merged List:", merged_list)
