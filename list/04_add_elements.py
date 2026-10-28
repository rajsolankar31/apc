# Program 4: Create a list of numbers. Add one at end, one at beginning, one at a specific position

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

end_val = int(input("Enter a number to add at the end: "))
numbers.append(end_val)

begin_val = int(input("Enter a number to add at the beginning: "))
numbers.insert(0, begin_val)

pos = int(input("Enter position to insert at: "))
val = int(input("Enter number to insert: "))
numbers.insert(pos, val)

print("Updated list:", numbers)
