# Program 24: Rotate a list left and right by one position

elements = []
n = int(input("Enter number of elements in the list: "))
for i in range(n):
    val = input(f"Enter element {i+1}: ")
    elements.append(val)

print("\nOriginal list:", elements)

if len(elements) > 0:
    # Rotate left by one position: first element moves to the end
    left_rotated = elements[1:] + elements[:1]
    
    # Rotate right by one position: last element moves to the front
    right_rotated = elements[-1:] + elements[:-1]

    print("Left rotated by 1 position:", left_rotated)
    print("Right rotated by 1 position:", right_rotated)
else:
    print("List is empty, cannot rotate.")
