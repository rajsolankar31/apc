# Program 15: Second Largest Element
# Find the second largest element in a list

numbers = []
n = int(input("How many numbers? "))
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("List:", numbers)
largest = numbers[0]
second_largest = None
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num
if second_largest is not None:
    print(f"Second largest element: {second_largest}")
else:
    print("No second largest element found.")
